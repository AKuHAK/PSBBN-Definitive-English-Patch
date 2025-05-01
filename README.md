# PSBBN Definitive English Patch

This is the Definitive English Patch for Sony's "PlayStation Broadband Navigator" software (also known as BB Navigator or PSBBN) for the "PlayStation 2" (PS2) video game console.

PSBBN is official Sony software for the PlayStation 2, released exclusively in Japan. Introduced in 2002 as a replacement for the PS2’s OSD, it required both a hard drive and a network adapter to function. It added many new features:
- Launching games from the hard drive in the Game Channel
- Accessing online channels
- Downloading full games, demos, videos, and pictures
- Ripping audio CDs and transferring music to MiniDisc recorders in the Music Channel
- Watching videos in the Movie Channel
- Transferring photos from a digital camera and viewing them in the Photo Channel

This project aims to translate PSBBN from Japanese to English, introduce modern features, and make it a viable daily driver in 2025 and beyond.

You can find out more about the PSBBN software on [Wikipedia](https://en.wikipedia.org/wiki/PlayStation_Broadband_Navigator) and on my [YouTube channle](https://www.youtube.com/@CosmicScaleFactor).

# Donations  
If you appreciate my work and want to support the ongoing development of the PSBBN Definitive English Patch and other PS2-related projects, [you can donate to my Ko-Fi here](https://ko-fi.com/cosmicscale).

This project uses [webhook.site](https://webhook.site/) to automatically contribute game artwork and report missing artwork to the [PSBBN Art Database](https://github.com/CosmicScale/psbbn-art-database). As the project has grow in popularity, we're exceeding the limit offered by a free account. A paid subscription costs $9/month or $90/year, donations help fund this.

## Video demonstration of PSBBN:

[![PSBBN in 2024](https://github.com/user-attachments/assets/298c8c0b-5726-4485-840d-9d567498fd95)](https://www.youtube.com/watch?v=kR1MVcAkW5M)

## Patch Features
- A full English translation of the stock Japanese BB Navigator version 0.32
- All binaries, XML files, textures, and pictures have been translated*
- Compatible with any fat model PS2 console as well as PS2 Slim SCPH-700xx models with an [IDE Resurrector](https://gusse.in/shop/ps2-modding-parts/ide-resurrector-origami-v0-7-flex-cable-for-ps2-slim-spch700xx/) or similar mod, regardless of region
- DNAS authorization checks bypassed to enable online connectivity
- Online game channels from Sony, Hudson, EA, Konami, Capcom, Namco, and KOEI have been translated into English. Hosted courtesy of vitas155 at [psbbn.ru](https://psbbn.ru/)
- "Audio Player" feature re-added to the Music Channel from an earlier release of PSBBN, allowing compatibility with NetMD MiniDisc Recorders
- Associated manual pages and troubleshooting regarding the "Audio Player" feature translated and re-added to the user guide
- Japanese qwerty on-screen keyboard replaced with US English on-screen keyboard**

## New to version 2.0
- Large HDD support: no longer limited to 128 GB. It now supports larger drives, with 128 GB allocated to the PlayStation File System (PFS) and up to 2 TB allocated to exFAT for PS2 games.
- Supports launching over 700 PS1/PS2 games from the PSBBN Game Channel
- Supports launching homebrew apps from the Game Channel with [wLaunchELF](https://github.com/ps2homebrew/wLaunchELF), [Retro GEM Disc Launcher](https://github.com/CosmicScale/Retro-GEM-PS2-Disc-Launcher) and [OPL](https://github.com/ps2homebrew/Open-PS2-Loader)/[NHDDL](https://github.com/pcm720/nhddl) pre-insatlled
- Set a custom size for your music partition. Original limit of 5 GB allowed the storage of around 7 albums. Now the partition can be up to 40 GB for around 60 albums
- exFAT partition for easy install of PS2 games
- PS2 Linux is pre-installed. See [General Notes](#general-notes) for details
- Bandai and SCEI online channels have been added to the Game Channel
- Some minor fixes to the English translation
### Updates:
- Added Game ID support for the Pixel FX Retro GEM. Works for both PS1 and PS2 games
- PS2 games now launch up to 5 seconds faster
- Resolved conflict with mass storage devices (USB, iLink, MX4SIO). Games now launch without issues if these devices are connected
- Apps now automatically update when you sync your games
- The art downloader has been improved to grab significantly more artwork
- Improved error handling in the PSBBN installer script
- The setup script has been modified to work on live Linux environments without issues
- Added support for Arch-based and Fedora-based Linux distributions in addition to Debian
- Added confirmation prompts to the PSBBN installer script when creating partitions
- PSBBN image updated to version 2.01:
  - Set USB keyboard layout to US English. Press `ALT+~` to toggle between kana and direct input
  - Minor corrections to the English translation
- Added [Open PS2 Loader](https://github.com/ps2homebrew/Open-PS2-Loader) and [Launch Disc](https://github.com/CosmicScale/Retro-GEM-PS2-Disc-Launcher) to the Game Channel
- The Game Installer script has been updated to create and delete game partitions as needed. Say goodbye to those annoying "Coming soon..." placeholders!
- Files placed in the `CFG`, `CHT`, `LNG`, `THM`, and `APPS` folders on your PC will now be copied to the PS2 drive during game sync
- Added Game ID support for MemCard Pro 2 and SD2PSX
- The scripts now auto-update when an update is available
- Optimised art work
- Art downloads from IGN are now automatically contributed to the [PSBBN art database](https://github.com/CosmicScale/psbbn-art-database), and missing artwork is also automatically reported. Manual submissions are welcome, see the [PSBBN art database GitHub page](https://github.com/CosmicScale/psbbn-art-database) for details
- [OPL-Launcher-BDM](https://github.com/CosmicScale/OPL-Launcher-BDM) has been replaced by [BBN Launcher (BBNL)](https://github.com/pcm720/bbnl)
- Added [Neutrino](https://github.com/rickgaiser/neutrino) support. You can now choose between [Open PS2 Loader](https://github.com/ps2homebrew/Open-PS2-Loader) and [Neutrino](https://github.com/rickgaiser/neutrino) as your game launcher
- [Open PS2 Loader](https://github.com/ps2homebrew/Open-PS2-Loader) updated to version 1.2.0-Beta-2201-4b6cc21:
  - Limited max BDM UDMA mode to UDMA4 to avoid compatibility issues with various SATA/IDE2SD adapters
- Added a manual for PS1 games. It can be accessed in the Game Channel by selecting a game, pressing Triangle, and then selecting `Manual`
- Transitioned to [BBN Launcher (BBNL)](https://github.com/pcm720/bbnl) version 2.0:
  - Dropped APA support in favor of loading [OPL](https://github.com/ps2homebrew/Open-PS2-Loader), [POPStarter](https://bitbucket.org/ShaolinAssassin/popstarter-documentation-stuff/wiki/Home), [Neutrino](https://github.com/rickgaiser/neutrino), and configuration files from the exFAT partition to speed up initialization.
  - Moved [BBNL](https://github.com/pcm720/bbnl) to the APA header to further improve loading times.
  - Removed dependency on renamed [POPStarter](https://bitbucket.org/ShaolinAssassin/popstarter-documentation-stuff/wiki/Home) ELF files to launch PS1 VCDs; [POPStarter](https://bitbucket.org/ShaolinAssassin/popstarter-documentation-stuff/wiki/Home) is now launched directly with a boot argument.
  - [NHDDL](https://github.com/pcm720/nhddl) now launches in ATA mode, improving startup time and avoiding potential error messages.
- Updated [Neutrino](https://github.com/rickgaiser/neutrino) to version 1.6.1
- Updated [NHDDL](https://github.com/pcm720/nhddl) to version MMCE + HDL Beta 4.17
- Added cover art from the [OPL Manager Art DB backups](https://oplmanager.com/site/index.php?backups). Artwork for PS2 games is now displayed in OPL/NHDDL
- Added homebrew support to the `03-Game-Installer.sh` script. `ELF` files placed in the local `games/APPS` folder on your PC will be installed and appear in the Game Channel in PSBBN and the Apps tab in OPL
- Apps now support Game ID for both the the Pixel FX Retro GEM and MemCard Pro/SD2PSX
- Added support for the [Save Application System (SAS)](https://ps2wiki.github.io/sas-apps-archive/). `PSU` files can now also be placed in the local `games/APPS` folder on your PC and will be installed by the `03-Game-Installer.sh` script
- Added support for HDD-OSD to the `03-Game-Installer.sh` script. 3D icons are now downloaded from the [HDD-OSD Icon Database](https://github.com/cosmicscale/hdd-osd-icon-database)
- New script: `04-Extras.sh`. Added ability to install HDD-OSD and [PlayStation 2 Basic Boot Loader (PS2BBL)](https://israpps.github.io/PlayStation2-Basic-BootLoader/)  


## New installation scripts

These scripts are essential for unlocking all the new features exclusive to version 2.0. The scripts require an x86-64 Linux environment. If Linux is not installed on your PC, you can use a live Linux environment on a bootable USB drive, [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install), or a virtual machine. Debian-based distributions using `apt`, Arch-based distributions using `pacman`, and Fedora-based distributions using `dnf` are supported. You will require a HDD/SSD for your PS2 that is larger than 200 GB, ideally 500 GB or larger. I highly recommend a SSD for better performance. You can connect the HDD/SSD to your PC either directly via SATA or using a USB adapter.

## Video Tutorial:

[![PSBBN Definitive English Patch 2.0](https://github.com/user-attachments/assets/d60dc4ff-85f8-4fb4-8acb-201b063545b0)](https://www.youtube.com/watch?v=sHz0yKYybhk)

<span style="font-size: 17px; font-weight: bold;">It is highly recommended to install the scripts using the following command to enable automatic updates:</span>
```
git clone https://github.com/CosmicScale/PSBBN-Definitive-English-Patch.git
```
If you have not used Git before, you might need to install it first. On Debian-based distributions, it can be installed with the following command:
```
sudo apt install git
```

### Setup script:
`01-Setup.sh` installs all the necessary dependencies for the other scripts and must be run first.

### PSBBN installer script:
`02-PSBBN-Installer.sh` fully automates the installation of PSBBN:

- Downloads and installs the latest version of the **PSBBN Definitive English Patch** from archive.org
- Installs the [POPS binaries](https://bitbucket.org/ShaolinAssassin/popstarter-documentation-stuff/wiki/Home)
- Creates partitions for the Music Channel and POPS (to store PS1 games), with user-defined sizes on the first 128 GB of the drive.
- All remaining space up to 128 GB is set aside for [BBN Launcher](https://github.com/pcm720/bbnl) partitions, used to launch games and apps.
- Runs [APA-Jail](#apa-jail), creating an exFAT partition using all remaining disk space beyond the first 128 GB (up to 2 TB)

### Game installer script: 
`03-Game-Installer.sh` fully automates the installation of PS1 and PS2 games, as well as homebrew apps. Simply place your files in the `games` folder on your computer: PS2 `ISO` or `ZSO` files in the `CD`/`DVD` folders, PS1 `VCD` files in the `POPS` folder, and `ELF` or [SAS-compliant](#save-application-system-sas) `PSU` files in the `APPS` folder.

The script will:
- Gives you a choice of [Open PS2 Loader (OPL)](https://github.com/ps2homebrew/Open-PS2-Loader) or [Neutrino](https://github.com/rickgaiser/neutrino) for the game launcher
- Synchronise the games and apps on your PC with your PS2's drive
- Create all assets
- Downloads artwork for the PSBBN Game Channel from the [PSBBN Art Database](https://github.com/CosmicScale/psbbn-art-database) or IGN if not found in the database
- Automatically contributes game artwork downloaded from IGN and reports missing artwork to the [PSBBN Art Database](https://github.com/CosmicScale/psbbn-art-database)
- Downloads cover art for PS2 games from the [OPL Manager art database](https://oplmanager.com/site/?backups) for display in [OPL](https://github.com/ps2homebrew/Open-PS2-Loader)/[NHDDL](https://github.com/pcm720/nhddl)
- Downloads icons for use with HDD-OSD/Browser 2.0 from the [HDD-OSD Icon Database](https://github.com/cosmicscale/hdd-osd-icon-database)
- Creates [BBN Launcher](https://github.com/pcm720/bbnl) partitions, making games and apps launchable from the PSBBN Game Channel
- Creates a `conf_apps.cfg` file so apps can be displayed and launched from [OPL](https://github.com/ps2homebrew/Open-PS2-Loader)

To add or delete games/apps, simply add or remove them from the `games` folder on your computer, then run the script again to synchronise.

The Game Channel groups items into PS1 games, PS2 games, and homebrew apps. PS1 and PS2 games are sorted alphabetically and organized by game series, with series ordered by release date. Homebrew apps are sorted alphabetically, while SAS apps are further divided into sub-groups based on app type (system, game, emulator, etc.).

By default, the `games` directory is located in the same directory where you installed the scripts. If you need to change its location, edit `03-Game-Installer.sh` and modify the `GAMES_PATH` variable. Alternatively, you can replace the `games/CD`, `games/DVD`, and `games/POPS` directories with a symbolic link that points to the storage location of your games. Another option is to create symbolic links in the `CD`, `DVD`, or `POPS` subdirectories, linking to the individual `ISO`, `ZSO`, or `VCD` files that you wish to sync.

### Extras script: 
`04-Extras.sh` installs optional extras:
1. Install HDD-OSD/Browser 2.0 - an updated version of the stock OSD shipped with every PS2 console, but with added HDD support.
2. Install [PlayStation 2 Basic Boot Loader (PS2BBL)](https://israpps.github.io/PlayStation2-Basic-BootLoader/) - a simple PS2 bootloader that handles system initialisation and ELF programs execution. With this bootloader, holding a button on the controller during startup determines which application is launched.
3. Uninstall [PlayStation 2 Basic Boot Loader (PS2BBL)](https://israpps.github.io/PlayStation2-Basic-BootLoader/)

## Notes:
### General:
- PSBBN requires a Fat PS2 console (SCPH-3000x to SCPH-500xx) with an expansion bay and an [official Sony Network Adapter](#known-issueslimitations-of-psbbn), or a PS2 Slim SCPH-700xx model with an [IDE Resurrector](https://gusse.in/shop/ps2-modding-parts/ide-resurrector-origami-v0-7-flex-cable-for-ps2-slim-spch700xx/) or similar mod. It is also compatible with the SCPH-10000 to SCPH-18000 models with an official external HDD, as long as the drive in the enclosure has been replaced with one that is 200 GB or larger.
- For expansion bay type consoles, I would highly recommend using a **Kaico or BitFunx IDE to SATA Upgrade Kit**
- A SATA SSD is also highly recommended. The **Kingston A400 SSDs** have been tried and tested with PSBBN and work very well. The improved random access speed over a HDD really makes a big difference to the responsiveness of the PSBBN interface.
- PS2 games must be in ISO or ZSO format. PS1 games must be in VCD format. Apps must be in the `ELF` or [SAS-compliant](#save-application-system-sas) `PSU` format
- PSBBN takes longer to start when there’s no active internet connection
- PS2 Linux is pre-installed. Wait until the `PlayStation 2` icon is displayed, then hold any button on the controller and keep holding it until the spinning orbs stop. PS2 Linux will then boot.
- PS2 Linux requires a USB keyboard; a mouse is optional but recommended
- The `root` password for Linux is `password`. There is also a `ps2` user account with the password set as `password`
- If the shortcut to [OPL](https://github.com/ps2homebrew/Open-PS2-Loader)/[NHDDL](https://github.com/pcm720/nhddl) in the Navigator Menu displays the error "Game not found," remove the shortcut. You can then manually re-add it from the Game Channel
- To quit PS1 games, press `L1 + SELECT + START`
- If you are using [OPL](https://github.com/ps2homebrew/Open-PS2-Loader) as your game launcher, to quit PS2 games, press `L1 + L2 + R1 + R2 + SELECT + START` and to power off the console press `L1 + L2 + L3 + R1 + R2 + R3`

### OPL:
[Open PS2 Loader (OPL)](https://github.com/ps2homebrew/Open-PS2-Loader) is a 100% open source game and application loader for the PS2.
- If you selected [Open PS2 Loader (OPL)](https://github.com/ps2homebrew/Open-PS2-Loader) as your game launcher, per-game settings assigned in OPL are reflected when launching games from the PSBBN Game Channel
- If OPL freezes at startup, delete any existing OPL configuration files from your PS2 Memory Cards or connected USB devices.
- To display the games list in OPL, make sure a PS2 memory card is inserted into your console, launch OPL and adjust the following settings:
1. Settings > HDD (APA) Start Mode: Off
2. Settings > BDM Start Mode: Auto
3. Settings > BDM Devices > HDD (GPT/MBR): On
4. Settings > Save Changes

### Neutrino and NHDDL:
[Neutrino](https://github.com/rickgaiser/neutrino) is a lightweight device emulator for PS2. [NHDDL](https://github.com/pcm720/nhddl) is a frontend for Neutrino.
- If you selected [Neutrino](https://github.com/rickgaiser/neutrino) as your game launcher, per-game settings assigned in [NHDDL](https://github.com/pcm720/nhddl) are reflected when launching games from the PSBBN Game Channel
- [Neutrino](https://github.com/rickgaiser/neutrino) does not support compressed `ZSO` files. If `ZSO` files are found in your `games` folder, they will be automatically decompressed to `ISO` files by the `03-Game-Installer.sh` script

### Save Application System (SAS):

Save Application System (SAS) is a new standard for distributing homebrew applications for the PS2. Currently in beta, but already has over 20 apps available for download on the [Save Application System Apps Archive](https://ps2wiki.github.io/sas-apps-archive/) with many more coming soon. All SAS-compliant apps come packed in a `PSU` file and include icons and metadata, making it the recommended way to install homebrew on PSBBN.

### PlayStation 2 Basic Boot Loader (PS2BBL):
If you choose to install the [PlayStation 2 Basic Boot Loader (PS2BBL)](https://israpps.github.io/PlayStation2-Basic-BootLoader/), the console will auto-boot into PSBBN unless the `cross` button is held during startup, in which case HDD-OSD will be launched instead (if installed).
Launch keys and other settings for [PS2BBL](https://israpps.github.io/PlayStation2-Basic-BootLoader/) can be modified by editing the `CONFIG.INI` file stored on the internal drive at `__sysconf/PS2BBL`, more info can be found [here](https://israpps.github.io/PlayStation2-Basic-BootLoader/documentation/configuration.html).

### Game ID:
Game ID for both the Retro GEM, MemCard Pro 2, and SD2PSX is fully supported when launching PS1 games, PS2 games, and homebrew apps from the Game Channel.

If you have a Retro GEM, I would highly recommend that you install the [Retro GEM Game ID Resetter](https://github.com/CosmicScale/Retro-GEM-GameId-Resetter) on your PS2 Memory Card. With this app, when you quit a game, the Game ID is reset, and the Retro GEM settings are returned to global.

### Launch Disc:
**Launch Disc** loads the [Retro GEM Disc Launcher](https://github.com/CosmicScale/Retro-GEM-PS2-Disc-Launcher) application.

For physical PlayStation game discs:
- Sets the Retro GEM Game ID
- Adjusts the PlayStation driver's video mode, if needed, to ensure imports play in the correct mode

For physical PlayStation 2 game discs:
- Sets the Retro GEM Game ID
- Skips the PlayStation 2 logo check, allowing MechaPwn users to launch imports and master discs

Recommended usage:
- Add a shortcut for **Launch Disc** to the **Navigator Menu** if it is not there already
- Press `SELECT` to open the **Navigator Menu**
- Insert a game disc
- Select **Launch Disc** from the menu

### APA-Jail:

![APA-Jail Type-A2](https://github.com/user-attachments/assets/8c83dab7-f49f-4a77-b641-9f63d92c85e7)

APA-Jail, created and developed by [Berion](https://www.psx-place.com/resources/authors/berion.1431/), enables the PS2's APA partitions to coexist with an exFAT partition. This setup allows PSBBN to access the first 128 GB of the HDD/SSD directly. All remaining space on the drive (up to 2 TB) is formatted as exFAT.

An application called [BBN Launcher](https://github.com/pcm720/bbnl) resides on the APA partitions, a [pre-release build of Open PS2 Loader](https://github.com/ps2homebrew/Open-PS2-Loader) and [Neutrino](https://github.com/rickgaiser/neutrino) reside on the exFAT partition, along with the PS2 games in the `ISO` or `ZSO` format.

The exFAT partition can be accessed on a PC and on the PS2 by [BBN Launcher](https://github.com/pcm720/bbnl), a [pre-release build of Open PS2 Loader](https://github.com/ps2homebrew/Open-PS2-Loader) and [Neutrino](https://github.com/rickgaiser/neutrino).

[BBN Launcher](https://github.com/pcm720/bbnl) directs [Open PS2 Loader](https://github.com/ps2homebrew/Open-PS2-Loader) or [Neutrino](https://github.com/rickgaiser/neutrino) to launch specific PS2 games.

<font size="4"><b>Warning: Creating new partitions manually on your PS2 drive (e.g., with wLaunchELF) and exceeding the 128 GB limit will cause drive corruption.</b></font>

## Legacy versions of the PSBBN Definitive English Patch

<details>
<summary>Click to expand</summary>

### Version History

**v1.2 - 4th September 2024**
- Fixed a bug on the Photo Channel that could potentially prevent the Digital Camera feature from being launched.
- Fixed formatting issues with a number of error messages where text was too long to fit on the screen.
- Various small adjustments and corrections to the translation throughout.

**v1.1.1 - 8th March 2024**
**NEW**  
- X11 has been set to run in English. The restore, move, resize, minimize, and close buttons now show in English while using the NetFront web browser. When saving files, time stamps now also display in English formatting.

**v1.1 - 5th March 2024**
**NEW**  
- The NetFront web browser is now in English. The browser can be accessed by going through the "Confirm/Change" network setting dialogs, then selecting "Change router settings".
- Atok user manual has been translated.

**BUG FIXES**  
- **General**: When a game disc was inserted while on the Top Menu, it would cause the console to freeze.  
- **Music Channel**: The number of times a track had been checked-out to a MiniDisc recorder was not displayed correctly.  
- A number of typos have been fixed.

**v1.0 - 21st September 2023**
- Initial release.

### Installation Instructions
---
There are two ways to install this English patch:

1. [PS2 HDD RAW Image Install](#ps2-hdd-raw-image-install): Use this method if you have access to a PC and a way to connect your PS2 HDD/SSD to your computer. This is the most straightforward option. All data on the HDD will be lost.

2. [Patch an existing PSBBN install](#patch-an-existing-psbbn-install): Use this method if you already have an existing PSBBN install on your PlayStation 2 console. Also, follow these instructions to install future patch updates. No data will be lost.

#### PS2 HDD RAW Image Install
---
**What You Will Need:**
- Any fat model PS2 console*
- An official Sony Network Adapter
- A compatible HDD or SSD (IDE or SATA with an adapter). The drive must be 120 GB or larger
- A way to connect the PS2 HDD to a PC
- 120 GB of free space on your PC to extract the files
- Disk imaging software

**Installation Procedure:**
1. Download [PSBBN_English_Patched_v1.x.x_Image.7z](https://archive.org/download/playstation-broadband-navigator-psbbn-definitive-english-patch-v1.0/PSBBN_English_Patched_v1.2_Image.7z) and uncompress it.
`PSBBN_English_Patched_v1.x.x_HDD_RAW.img` is a raw PS2 disk image of the Japanese PlayStation BB Navigator Version 0.32 with the PlayStation Broadband Navigator (PSBBN) Definitive English Patch pre-installed.
2. To write this image to your PS2 HDD, you need disk imaging software. For Windows, I recommend using HDD Raw Copy ver. 1.10 portable. You can download it [here](https://hddguru.com/software/HDD-Raw-Copy-Tool/).

#### Patch an existing PSBBN install
---
**What You Will Need:**
- Any fat model PS2 console*
- An official Sony Network Adapter
- A compatible HDD or SSD (IDE or SATA with an adapter)
- An existing install of PSBBN software 0.32 on your PS2 console
- A Free McBoot Memory Card
- A USB flash drive formatted as FAT32
- A USB keyboard

**Installing the English Patch:**
1. Install the PSBBN software on your PS2 console if you haven't done so already. Either via a disk image or manually, see the section [Installing the Japanese PSBBN software](#installing-the-japanese-psbbn-software) below for details on a manual install.
2. Download [PSBBN_English_Patch_Installer_v1.x.x.zip](https://archive.org/download/playstation-broadband-navigator-psbbn-definitive-english-patch-v1.0/PSBBN_English_Patch_Installer_v1.2.zip) and unzip it on your PC.
3. Copy the files `kloader3.0.elf`, `config.txt`, `xrvmlinux`, `xrinitfs_install.gz`, and `PSBBN_English.tar.gz` to the root of a FAT32 formatted USB flash drive.
4. Connect the USB flash drive and a USB keyboard to the USB ports on the front of your PS2 console.
5. Turn the PS2 console on with your Free McBoot Memory Card inserted and load wLaunchELF.
6. Load `kloader3.0.elf` from the USB flash drive.
7. Eventually, you will be presented with a login prompt:  
     Type `root` and press enter.  
     Type `install` and press enter.
8. When you see the text `INIT: no more processes left in this runlevel`, hold the standby button down until the console powers off.

Remove your Free McBoot Memory Card. Power the console on and enjoy PSBBN in full English!

### Installing the Japanese PSBBN software
---
There are a number of ways this can be achieved. On a Japanese PlayStation 2 console with an **official PSBBN installation disc**, or with **Sony Utility Discs Compilation 3**.

To install via **Sony Utility Discs Compilation 3** you will need a way to boot backup discs on your console, be that a mod chip or a swap disc. If you are lucky enough to have a **SCPH-500xx** series console you can use the **MechaPwn** softmod.

Installing with Sony Utility Discs Compilation 3:

**Preparations:**
1. Download the **Sony Utility Discs Compilation 3** ISO from the Internet Archive [here](https://archive.org/details/sony-utility-disc-compilation-v3).
2. **SCPH-500xx consoles only**: Patch the ISO with the [Master Disc Patcher](https://www.psx-place.com/threads/playstation-2-master-disc-patcher-for-mechapwn.36547/).
3. Burn this ISO to a writable DVD. I recommend using [ImgBurn](https://www.imgburn.com).
4. **SCPH-500xx consoles only**: MechaPwn your PS2 console with the latest release candidate, currently [MechaPwn 3.0 Release Candidate 4 (RC4)](https://github.com/MechaResearch/MechaPwn/releases/tag/3.00-rc4). It is important that you use a version of MechaPwn that does not change the **Model Name** of your console or it will break compatibility with the Kloader app, we use later in this guide. Currently the latest stable version is not compatible. More details about exactly what MechaPwn does and how to use it can be found [here](https://github.com/MechaResearch/MechaPwn).
5. Format the PS2 HDD. In wLaunchELF press the `circle` button for **FileBrowser**, then select **MISC > HddManager**. Press `R1` to open the menu and select **Format**. When done, press `triangle` to exit.
6. Launch the **Sony Utility Discs Compilation 3** DVD on your console. **SCPH-500xx consoles only:** Insert your newly burnt **Sony Utility Discs Compilation 3** DVD into the DVD drive on your PS2 console. On the first screen of wLaunchELF, press the `circle` button for **FileBrowser**, then select **MISC > PS2Disc**. The DVD will launch. On all other model consoles, launch the **Sony Utility Discs Compilation 3** DVD any way you can (e.g. Mod chip/Swap disc).
7. After the disc loads, select **HDD Utility Discs > PlayStation BB Navigator Version 0.32** from the menu to begin the installation.

**Installation:**  
There's an excellent guide [here](https://bungiefan.tripod.com/psbbninstall_01.html) that talks you through the Japanese install. Because we have already formatted the hard drive, during the install you will be presented with a [different screen](https://bungiefan.tripod.com/psbbninstall_02.html). It's important that you select the 3rd install option. This will install PSBBN without re-formatting the HDD. When the install is complete you will be instructed to remove the DVD, do so but also remove your Free McBoot Memory Card, before pressing the `circle` button.

**Network Settings:**  
You will be asked to enter your network settings. Make sure your Ethernet cable is connected. Everything is still in Japanese, but it's relatively straightforward:
1. Press the `circle` button on the first screen.
2. On the next screen, select the **bottom** option, "Do not use PPPoE" and press `circle`.
3. On the next screen, select the **top** option, "Auto" for you IP address and press `circle`.
4. On the next screen, select the **top** option, "Auto" for DNS settings and press `circle`.
5. Press `right` on the d-pad to proceed to the next screen.
6. Select the **bottom** option, "Do not change router settings" and press `circle`.
7. Finally, press `circle` again to confirm your settings.

For your efforts you will be given a DNAS error. This is to be expected. We'll fix that next. Press `X` and feel free to explore your fresh install of the Japanese PSBBN.

**Disable DNAS Authentication:**  
1. Turn off the console and put your Free McBoot Memory Card back into a memory card slot.  
2. Turn the console on and load wLaunchELF.  
3. Go to **FileBrowser**. Navigate to `hdd0:/__contents/bn.conf/` and delete the file `default_isp.dat`. This will disable the DNAS checks.

**Please Note**
Before installing the English patch, you **must** power off your console to standby mode by holding the reset button. Failure to do so will cause issues with Kloader.

### Notes
---
\* Also compatible with the PS2 Slim SCPH-700xx models with an [IDE Resurrector](https://gusse.in/shop/ps2-modding-parts/ide-resurrector-origami-v0-7-flex-cable-for-ps2-slim-spch700xx/) or similar mod. [PS2 HDD RAW Image Install](#ps2-hdd-raw-image-install) is not compatible with early model Japanese PS2 consoles (SCPH-10000, SCPH-15000 and SCPH-18000) that have an external HDD due to space limitations (unless the stock drive is replaced with a 120+ GB drive). When [patching an existing PSBBN install](#patch-an-existing-psbbn-install), Kloader might have compatibility issues with early model Japanese PS2 consoles (SCPH-10000, SCPH-15000 and SCPH-18000).  
- Use OPL-Launcher to launch PS2 games from the Game Channel. More details can be found [here](https://github.com/ps2homebrew/OPL-Launcher).
- Lacks support for large HDDs, drives larger than 130 GB cannot be taken full advantage of. PSBBN can only see the first 130,999 MB of data on your HDD/SSD (as reported by wLaunchELF). If there is 131,000 MB or more on your HDD/SSD, PSBBN will fail to launch. Delete data so there is less than 131,000 MB used, and PSBBN will launch again. Be extra careful if you have installed via the [PS2 HDD RAW Image](#ps2-hdd-raw-image-install) on a drive larger than 120 GB, going over 130,999 MB will corrupt the drive.
- You may need to manually change the title of your "Favorite" folders if they were created before you [Patched an existing PSBBN install](#patch-an-existing-psbbn-install).

</details>

## Troubleshooting

### Problems Launching PSBBN
When you connect the drive to your PS2 console and power it on, PSBBN should automatically launch.

#### Fat PS2 console models SCPH-3000x-500xx:
If your console boots to the regular OSD or freezes at the `PlayStation 2` logo, it means that your drive has not been recognised or you are experiencing another hardware issue. You should check the following:
1. Make sure you are using an official Sony Network Adapter; 3rd-party adapters are not supported
2. Ensure the network adapter and drive are securely connected to the console
3. Check that the connectors on the console and network adapter are clean and free of dust/debris
4. If using a SATA mod, make sure it has been installed correctly
5. Try using a different HDD/SSD
7. Try using a different IDE converter/SATA mod
8. Try a different official Sony Network Adapter

#### Slim PS2 console model SCPH-700xx:
If you are using a PS2 Slim SCPH-700xx model with an [IDE Resurrector](https://gusse.in/shop/ps2-modding-parts/ide-resurrector-origami-v0-7-flex-cable-for-ps2-slim-spch700xx/) or similar mod, download the [External HDD Drivers](https://israpps.github.io/FreeMcBoot-Installer/test/8_Downloads.html). Extract the files and place `hddload.irx`, `dev9.irx`, and `atad.irx` in the appropriate system folder for your region on an official Sony PS2 Memory Card:

| Region   | Folder Name   |
|----------|-------------- |
| Japanese | BIEXEC-SYSTEM |
| American | BAEXEC-SYSTEM |
| Asian 	 | BAEXEC-SYSTEM |
| European | BEEXEC-SYSTEM |
| Chinese  | BCEXEC-SYSTEM |

If, after doing so, the console freezes at the `PlayStation 2` logo, the most likely cause is an incompatible IDE to SD card adapter.

### Problems Launching Games
If games do not appear in the games list in [NHDDL](https://github.com/pcm720/nhddl) or [OPL](https://github.com/ps2homebrew/Open-PS2-Loader) after following the instructions [above](#opl), and fail to launch from the PSBBN Game Channel, try the following:

1. If you have a [mod chip](#known-issueslimitations-of-psbbn), disable it
2. Re-run `03-Game-Installer.sh` and select a different game launcher
3. Connect the PS2 HDD/SSD directly to your PC using an internal SATA connection or a different USB adapter, then re-run `02-PSBBN-Installer.sh`
4. Try using a different HDD/SSD and re-run `02-PSBBN-Installer.sh`
5. Try using a different IDE converter/SATA mod on your console

## Known Issues
- PSBBN only supports dates up to the end of 2030. When setting the time and date, the year must be set to 2030 or below.  
- PSBBN will freeze when launching apps if a mod chip is detected. To use PSBBN, mod chips must be disabled.  
- PSBBN will freeze at the "PlayStation 2" logo when booting, if a 3rd party, unofficial HDD adapter is used. An official Sony Network Adapter is required.  
- When using a drive larger than 2 TB, the first 128 GB will be allocated to the PlayStation File System (PFS), and the next 2 TB will be formatted as an exFAT partition. Any remaining space beyond that will be unusable.
- HDD-OSD may report drives larger than 960 GB as broken.

\* Instances in feega where some Japanese text couldn't be translated due to it being hard-coded in an encrypted file. Atok software has not been translated.  
\** The default on-screen keyboard is set to Japanese. However, a US English on-screen keyboard has been added, though you’ll need to press the `SELECT` button multiple times to switch to it. There's a bug where spacebar doesn't work on the US English on-screen keyboard, but you can enter a space by pressing the `triangle` button on the controller instead.

## Credits
- PSBBN Definitive English Patch project by [CosmicScale](https://github.com/CosmicScale)
- PSBBN English translation by [CosmicScale](https://github.com/CosmicScale)
- `01-Setup.sh`, `02-PSBBN-Installer.sh`, `03-Game-Installer.sh`, `04-Extras.sh`, `art_downloader.js` written by [CosmicScale](https://github.com/CosmicScale)
- Contains code from `list_builder.py` from [XEB+ neutrino Launcher Plugin](https://github.com/sync-on-luma/xebplus-neutrino-loader-plugin) by [sync-on-luma](https://github.com/sync-on-luma), modified by [CosmicScale](https://github.com/CosmicScale)
- Contains data from `TitlesDB_PS1_English.txt` and `TitlesDB_PS2_English.txt` from the [Title Database Scrapper](https://github.com/GDX-X/Title-Database-Scrapper), modified by [CosmicScale](https://github.com/CosmicScale)
- [BBN Launcher](https://github.com/pcm720/bbnl) written by [pcm720](https://github.com/pcm720) and [CosmicScale](https://github.com/CosmicScale)
- [Open PS2 Loader](https://github.com/ps2homebrew/Open-PS2-Loader) with BDM contributions from [KrahJohlito](https://github.com/KrahJohlito) and Auto Launch modifications by [CosmicScale](https://github.com/CosmicScale)
- [Neutrino](https://github.com/rickgaiser/neutrino) by [Rick Gaiser](https://github.com/rickgaiser)
- [NHDDL](https://github.com/pcm720/nhddl) written by [pcm720](https://github.com/pcm720)
- [POPStarter](https://bitbucket.org/ShaolinAssassin/popstarter-documentation-stuff/wiki/Home) written by KrHACKen
- [Retro GEM Disc Launcher](https://github.com/CosmicScale/Retro-GEM-PS2-Disc-Launcher) written by [CosmicScale](https://github.com/CosmicScale)
- Uses APA-Jail code from the [PS2 HDD Decryption Helper](https://www.psx-place.com/resources/ps2-hdd-decryption-helper.1507/) by [Berion](https://www.psx-place.com/members/berion.1431/)
- [APA Partition Header Checksumer](https://www.psx-place.com/resources/apa-partition-header-checksumer.1057/) by [Pink1](https://www.psx-place.com/members/pink1.1907/) and [Berion](https://www.psx-place.com/members/berion.1431/). Linux port by [Bucanero](https://github.com/Bucanero)
- `PSU Extractor.elf` written by [Bucanero](https://github.com/Bucanero) from the [PS2 HDD Decryption Helper](https://www.psx-place.com/resources/ps2-hdd-decryption-helper.1507/) project
- `ziso.py` from [Open PS2 Loader](https://github.com/ps2homebrew/Open-PS2-Loader) written by Virtuous Flame
- `icon_sys_to_txt.py` written by [NathanNeurotic (Ripto)](https://github.com/NathanNeurotic)
- `mkfs.exfat` from [exfatprogs](https://github.com/exfatprogs/exfatprogs)
- [PlayStation 2 Basic Boot Loader (PS2BBL)](https://github.com/israpps/PlayStation2-Basic-BootLoader) written by [Matías Israelson (israpps)](https://github.com/israpps)
- Online channels resurrected, translated, maintained and hosted by vitas155 at [psbbn.ru](https://psbbn.ru/)
- PlayStation Now! and Konami online channels re-translated by [CosmicScale](https://github.com/CosmicScale)
- [PSBBN Art Database](https://github.com/CosmicScale/psbbn-art-database) created and maintained by [CosmicScale](https://github.com/CosmicScale)
- [HDD-OSD Icon Database](https://github.com/CosmicScale/HDD-OSD-Icon-Database) created and maintained by [CosmicScale](https://github.com/CosmicScale)
- Uses PS2 cover art from the [OPL Manager Art DB backups](https://oplmanager.com/site/index.php?backups)
- Uses App icons from [OPL B-APPS Cover Pack](https://www.psx-place.com/resources/opl-b-apps-cover-pack.1440/) and [OPL Discs & Boxes Pack](https://www.psx-place.com/resources/opl-discs-boxes-pack.1439/) courtesy of [Berion](https://www.psx-place.com/resources/authors/berion.1431/)
- Thanks to everyone on the [Save Application System team](https://ps2wiki.github.io/documentation/homebrew/PS2-App-System/SAS/index.html#Credits) for their ongoing work on the [Save Application System Apps Archive](https://ps2wiki.github.io/sas-apps-archive/)
- This project also uses [PFS Shell](https://github.com/ps2homebrew/pfsshell), [HDL Dump](https://github.com/ps2homebrew/hdl-dump), [wLaunchELF](https://github.com/ps2homebrew/wLaunchELF) and [PS1VModeNeg](https://github.com/ps2homebrew/PS1VModeNeg)
