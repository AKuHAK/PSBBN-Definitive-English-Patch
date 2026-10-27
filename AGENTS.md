# AGENTS.md — Technical Reference for AI Coding Assistants

This document contains architecture details, structural rules, and platform-specific workflows for AI agents working on `PSBBN-Definitive-Project` on macOS.

---

## 1. System Architecture Overview

PlayStation Broadband Navigator (PSBBN) runs on a modified 2.4.17 Linux kernel on the PlayStation 2. The hard drive uses the **APA (Advanced Programmable Architecture)** partitioning scheme rather than traditional MBR/GPT.

### 1.1. Partition Layout
- **APA Master Boot Record (MBR)**: Located at sector 0 and sector 4 (recovery).
- **PFS Partitions**: PlayStation File System partitions (`__system`, `__sysconf`, `__common`, `__contents`). Initialized by `pfsshell` via `initialize yes`.
- **EXT2 Partitions**: Standard Linux ext2 partitions:
  - `__linux.1`: Root filesystem (`/`), 1024 MB.
  - `__linux.2`: Linux swap, 128 MB.
  - `__linux.4`: Main BB Navigator binary and asset store (`/opt0`), 1024 MB.
  - `__linux.5`: Home directories (`/net`), 512 MB.
  - `__linux.6`: Temporary files (`/bntmp`), 128 MB.
  - `__linux.7`: System configurations and shortcuts (`/mnt`), 256 MB.
  - `__linux.9`: Channel applications (`/channels`), 2048 MB.
- **APA-Jail**: Injected into sector 0 (MBR partition 3) using Berion's APA-Jail specification (`apajail_magic_number`) to allow hybrid MBR access for OPL/fat partitions while preserving APA structure.

---

## 2. macOS Darwin Platform Shims & Workflows

macOS cannot natively mount APA or EXT2 filesystems with Linux permissions. Upstream solves this using `scripts/platform/darwin/lib.sh`:

1. **Staging**: Partitions are staged as directories inside `/tmp/psbbn-storage-${UID}/` (mapped from `${STORAGE_DIR}`).
2. **Import / Export**:
   - `psbbn_ext2_export`: Uses `debugfs` (from Homebrew `e2fsprogs`) to dump files from the slice.
   - `psbbn_ext2_import`: Uses `debugfs_apply.py` to write modified files back into the disk slice.
3. **Flushing to Hardware**:
   - On `umount`, slices are committed and written directly to the raw character device `/dev/rdiskX` using `dd`.
4. **Veto Daemon (`da-veto`)**:
   - Prevents macOS `diskarbitrationd` from auto-mounting slices and locking partitions during write operations.
   - Compiled from `scripts/helper/darwin-arm64/da-veto.c` with CoreFoundation and DiskArbitration frameworks.

---

## 3. Helper Tools Toolchain

All macOS helper tools reside in:
- `scripts/helper/darwin-x86_64/` (for Intel x86_64)
- `scripts/helper/darwin-arm64/` (for Apple Silicon ARM64)

Required binaries:
- `PFS Shell.elf`: AKuHAK's fork of `pfsshell` compiled with `mkpart <name> <size> EXT2` and `EXT2SWAP` support.
- `HDL Dump.elf`: `hdl_dump` (AKuHAK 8M branch).
- `PS2 APA Header Checksum Fixer.elf`: Recalculates and fixes APA header checksums in sector 0.
- `PSU Extractor.elf`: Extracts `.psu` save/icon containers.
- `da-veto`: DiskArbitration blocker daemon.
- `mkfs.exfat`: exFAT formatter for APA-Jail partition 3.

---

## 4. SSH & Live Debugging Architecture

OpenSSH server (`sshd`) and SFTP subsystem are pre-installed into `__linux.1`:
- Configuration file: `/etc/ssh/sshd_config`
  - `Subsystem sftp /usr/libexec/openssh/sftp-server`
  - `PermitRootLogin yes`
  - `PasswordAuthentication yes`
- Default credentials: user `bn`, password `bn` (hash: `$1$bnsalt12$rhP2dDKGxaO13SnMVV.Vk1` in `/etc/shadow`).
- Network setup: `/etc/sysconfig/network-scripts/ifcfg-eth0` defaults to `BOOTPROTO=dhcp`, `ONBOOT=yes`.
- When modifying Navigator on a live console, connect via SSH/SFTP or mount via `sshfs` to `/` directly.

---

## 5. Critical Instructions for Agents

1. **Do not use external `mkfs.ext2` tools**: Formatting of ext2 and ext2swap must remain inside `pfsshell` via `mkpart`.
2. **Do not add back games or music**: Keep the installer focused on bare BB Navigator without POPS, OPL, Neutrino, or `PP.*` partitions.
3. **Always preserve `bash` 5+ requirement**: macOS `/bin/bash` is 3.2 and lacks `declare -A` (associative arrays). Use `/usr/local/bin/bash`.
4. **Always unmount target disk before running installer**: Use `diskutil unmountDisk /dev/diskX`.
