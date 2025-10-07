import struct
import sys
import os
import subprocess

def get_disk_size_sectors(device: str) -> int:
    """
    Gets the total size of a disk or partition in GB, cross-platform.

    Args:
        device: A path to the device.

    Returns:
        The total size of the disk/partition in GB, or 0 on error.
    """
    try:
        if sys.platform == "darwin":  # macOS
            try:
                with open(device, 'rb') as f:
                    f.seek(0, os.SEEK_END)
                    size_bytes = f.tell()
                    sectors = int(size_bytes / 512)
                    if sectors == 0:
                        pass
                    else:
                        print(f"Sectors: {sectors}")
                        return sectors
            except Exception as e:
                print(f"Error opening device as file: {e}")
                pass

            result = subprocess.run(['diskutil', 'info', device], capture_output=True, text=True, check=True)
            output = result.stdout
            size_line = next((line for line in output.splitlines() if "Disk Size:" in line), None)
            if not size_line:
                raise ValueError("Could not find total size")
            # Extract the number of 512-Byte-Units
            units_str = size_line.split("exactly")[1].split("512-Byte-Units")[0].strip()
            print(f"Sectors: {units_str}")
            return int(units_str)

        elif sys.platform.startswith("linux"):  # Linux
            if os.path.ismount(device):
                statvfs = os.statvfs(device)
                size_bytes = statvfs.f_frsize * statvfs.f_blocks
                sectors = size_bytes // 512
                return sectors
            else:
                total, used, free = shutil.disk_usage(device)
                sectors = total // 512
                return sectors

        elif sys.platform == "win32":  # Windows
            import shutil
            total, _, _ = shutil.disk_usage(device)
            sectors = total // 512
            return sectors

        else:
            raise OSError("Unsupported platform")

    except (subprocess.CalledProcessError, ValueError, OSError, FileNotFoundError) as e:
        print(f"Error getting disk size: {e}")
        return 0

def apaCheckSum(header: bytes) -> int:
    """Calculate checksum for the header, ensuring 32-bit wraparound."""
    values = struct.unpack("256I", header)  # Interpret as 256 unsigned 32-bit integers (2 sectors)
    return sum(values[1:]) & 0xFFFFFFFF  # Ensure it stays within 32-bit range

def fix_checksum(device: str, file_handle=None, offset: int = 0):
    SECTOR_SIZE = 512
    TOTAL_SIZE = SECTOR_SIZE * 2  # Read first two sectors
    MAGIC_OFFSET = 0x100
    MAGIC_STRING = b"Sony Computer Entertainment Inc"
    CHECKSUM_OFFSET = 0

    if file_handle is None:
        with open(device, "r+b") as f:
            return fix_checksum(device, f, offset)

    f = file_handle
    # Move to the specified offset
    f.seek(offset)
    # Read the first two sectors (1024 bytes) from the offset
    sector = f.read(TOTAL_SIZE)

    if offset == 0:
        # Verify magic string at offset 0x100
        if sector[MAGIC_OFFSET:MAGIC_OFFSET + len(MAGIC_STRING)] != MAGIC_STRING:
            print("Magic string not found. Aborting.")
            return
    else:
        # Verify magic string at relative offset 4
        if sector[4:8] != b"APA\x00":
            print("Magic string 'APA\\x00' not found at relative offset 4. Aborting.")
            return

    # Compute checksum
    new_checksum = apaCheckSum(sector)
    current_checksum = struct.unpack("I", sector[CHECKSUM_OFFSET:CHECKSUM_OFFSET + 4])[0]

    # Only update if checksum is incorrect
    if new_checksum != current_checksum:
        print(f"Fixing APA checksum: {current_checksum:#010x} -> {new_checksum:#010x}")

        # Write new checksum
        new_sector = struct.pack("I", new_checksum) + sector[4:]
        f.seek(offset)
        f.write(new_sector)
        print("APA Checksum updated.")
    else:
        print("APA Checksum is already correct.")

def create_mbr_partitions(device: str):
    MAGIC_OFFSET = 0x100
    MAGIC_STRING = b"Sony Computer Entertainment Inc"
    SECTOR_SIZE = 512
    MIN_PS2_SIZE_GB = 15
    MAX_PS2_SIZE_GB = 128
    PARTITION_TYPE_PROTECTIVE = 0x42  # Possibly better alternatives exist
    PARTITION_TYPE_EXFAT = 0x07  # NTFS/exFAT

    with open(device, "r+b") as f:
        # Read first sector (MBR)
        mbr = f.read(SECTOR_SIZE)

        # Verify magic string at offset 0x100
        if mbr[MAGIC_OFFSET:MAGIC_OFFSET + len(MAGIC_STRING)] != MAGIC_STRING:
            print("Magic string not found. Aborting.")
            return

        # Check if MBR already contains partitions
        existing_partitions = mbr[446:510]
        # if any(existing_partitions):
        if 0:
            print("Warning: Existing MBR partitions detected!")
            for i in range(4):
                entry = existing_partitions[i*16:(i+1)*16]
                if entry[4] != 0:
                    start_lba = struct.unpack('<I', entry[8:12])[0]
                    size_lba = struct.unpack('<I', entry[12:16])[0]
                    size_gb = size_lba * SECTOR_SIZE / (1024 ** 3)
                    print(f"Partition {i+1}: Type {hex(entry[4])}, Start LBA {start_lba}, Size {size_gb:.2f} GB")
            confirm = input("Proceeding will overwrite MBR partitions. Type 'YES' to continue: ")
            if confirm != "YES":
                print("Operation aborted.")
                return

        # Get HDD size in GB
        disk_size_sectors = get_disk_size_sectors(device)
        if disk_size_sectors == 0:
            print("Failed to detect HDD size. Aborting.")
            return
        disk_size_gb = (disk_size_sectors * SECTOR_SIZE) // (1024 ** 3)
        print(f"Detected HDD size: {disk_size_gb}GB")
        if disk_size_gb < MIN_PS2_SIZE_GB:
            print("HDD size is less than the minimum required {MIN_PS2_SIZE_GB} GB. Aborting.")
            return

        # Determine default partition sizes
        default_ps2_size_gb = min(MAX_PS2_SIZE_GB, max(MIN_PS2_SIZE_GB, disk_size_gb - 1))
        exfat_size_gb = disk_size_gb - default_ps2_size_gb

        print(f"Default PS2 Partition: {default_ps2_size_gb}GB (Type 0x42)")
        print(f"Default ExFAT Partition: {exfat_size_gb}GB (Type 0x07)")

        # Ask user to confirm or change PS2 partition size
        user_input = input(f"Enter PS2 partition size in GB ({MIN_PS2_SIZE_GB}-{min(MAX_PS2_SIZE_GB, disk_size_gb - 1)}), default is {default_ps2_size_gb}: ")
        if user_input:
            try:
                ps2_size_gb = int(user_input)
                if ps2_size_gb < MIN_PS2_SIZE_GB or ps2_size_gb > min(MAX_PS2_SIZE_GB, disk_size_gb - 1):
                    print("Invalid size. Aborting.")
                    return
            except ValueError:
                print("Invalid input. Aborting.")
                # return
        else:
            ps2_size_gb = default_ps2_size_gb

        exfat_size_gb = disk_size_gb - ps2_size_gb

        print(f"PS2 Partition: {ps2_size_gb}GB (Type 0x42)")
        print(f"ExFAT Partition: {exfat_size_gb}GB (Type 0x07)")
        confirm = input("Confirm partition creation? Type 'YES' to proceed: ")
        if confirm != "YES":
            print("Operation aborted.")
            return

        # Create new partition table
        ps2_lba = int(ps2_size_gb * (1000 ** 3) / SECTOR_SIZE)
        new_mbr = bytearray(SECTOR_SIZE)
        new_mbr[:SECTOR_SIZE] = mbr[:SECTOR_SIZE]  # Copy existing MBR
        new_mbr[446:462] = struct.pack("<B3sB3sII", 0x00, b"\x00\x02\x00", PARTITION_TYPE_PROTECTIVE, b"\xFF\xFF\xFF", 1, ps2_lba - 1)
        new_mbr[462:478] = struct.pack("<B3sB3sII", 0x00, b"\x00\x00\x00", PARTITION_TYPE_EXFAT, b"\x00\x00\x00", ps2_lba, disk_size_sectors - ps2_lba - 34)
        new_mbr[510:512] = b"\x55\xAA"  # MBR signature

        # Write updated MBR
        f.seek(0)
        f.write(new_mbr)
        print("MBR partitions successfully created.")
        f.close()

        # Format the second partition as exFAT with 32KB cluster size
        if sys.platform == "darwin":  # macOS
            subprocess.run(["newfs_exfat", "-b", "32768", f"{device}s2"], check=True)
        elif sys.platform.startswith("linux"):  # Linux
            subprocess.run(["mkfs.exfat", "-s", "32", "-n", "PS2EXFAT", f"{device}2"], check=True)
        elif sys.platform == "win32":  # Windows
            subprocess.run(["format", f"{device}2", "/FS:exFAT", "/A:32K", "/V:PS2EXFAT", "/Q", "/Y"], check=True)
        else:
            raise OSError("Unsupported platform")

        print("Second partition formatted as exFAT with 32KB cluster size.")
        fix_checksum(device, 0)

if __name__ == "__main__":
    MAGIC_STRING = b"Sony Computer Entertainment Inc"
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} /dev/sdX")
        sys.exit(1)

    action = input("Choose action: 1) Fix checksum 2) Create partitions: 3) Update jail partition: ")
    if action == "1":
        offset_sectors = input("Enter LBA offset in 512-byte sectors (default is 0, hex format like 0x1400000): ")
        try:
            offset = int(offset_sectors, 16) * 512 if offset_sectors else 0
        except ValueError:
            print("Invalid input. Using default offset 0.")
            offset = 0
        fix_checksum(sys.argv[1], offset=offset)
    elif action == "2":
        create_mbr_partitions(sys.argv[1])
    elif action == "3":
        with open(sys.argv[1], "r+b") as f:
            # Verify magic string at offset 0x100
            f.seek(0x100)
            if f.read(len(MAGIC_STRING)) != MAGIC_STRING:
                print("Magic string not found. Aborting.")
                sys.exit(1)

            # Read jail offset
            f.seek(0xc)
            jail_offset = 512 * struct.unpack("<I", f.read(4))[0]
            print(f"Jail offset: {jail_offset:#010x}")

            # Verify APA magic string at jail offset + 4
            f.seek(jail_offset + 4)
            if f.read(4) != b"APA\x00":
                print("Magic string 'APA\\x00' not found at jail offset. Aborting.")
                sys.exit(1)
            test = input("Continue? ")

            # Write max possible 28-bit value at jail offset + 0x44
            max_28_bit_value = (1 << 28) - 1
            f.seek(jail_offset + 0x44)
            f.write(struct.pack("<I", max_28_bit_value))

            # Fix checksum at jail offset
            fix_checksum(sys.argv[1], f, jail_offset)

            print("Jail partition updated and checksum fixed.")
    else:
        print("Invalid selection.")
