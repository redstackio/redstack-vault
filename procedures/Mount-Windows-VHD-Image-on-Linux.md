---
id: b8832e7f-f1a3-4267-baaa-3248feb1032c
name: Mount-Windows-VHD-Image-on-Linux
type: procedure
verified: true
submitted: false
created_at: '2019-10-11T22:11:00.298490+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics: []
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - hypervisors
  - forensics
  - disk-analysis
commands:
  - '[[commands/guestmount-mount-vhd-file]]'
platforms:
  - Linux
tools:
  - '[[tools/libguestfs]]'
validated: true
---

# Mount-Windows-VHD-Image-on-Linux

## Summary

This procedure allows mounting a Windows Hyper-V Virtual Hard Disk (VHD) image on a Linux system using the guestmount tool from the libguestfs suite. It enables read-only access to the filesystem contents of the VHD for analysis, such as forensic investigation, malware examination, or data recovery without altering the original image.

## Description

VHD files are virtual disk formats used by Windows Hyper-V. Mounting them on Linux facilitates offline analysis of the disk contents, including browsing files, extracting artifacts, or inspecting for security incidents. The guestmount tool leverages libguestfs to attach the VHD as a loop device and mount it to a directory. This approach is read-only by default to preserve evidence integrity. It is particularly useful in red team scenarios for analyzing captured disk images or in blue team operations for incident response. The procedure assumes a fixed-size or dynamic VHD and works on most Linux distributions with libguestfs installed.

## Requirements

1. Linux host system (e.g., Ubuntu, Kali) with root or sudo access.
2. libguestfs-tools package installed.
3. The VHD image file accessible on the local filesystem.
4. Sufficient disk space in the mount directory for any temporary operations.
5. No write access needed, but ensure the mount point directory exists and is empty.

## Defense

Defensive measures and detection strategies:

- Monitor for libguestfs or guestmount executions in environments where disk image analysis is not expected, using process auditing tools like auditd or Sysmon.
- Restrict access to VHD files and mounting tools in forensic or analysis workstations to authorized personnel only.
- Use file integrity monitoring to detect unauthorized mounting or access to virtual disk images.

## Objectives

1. Safely mount the VHD image for read-only inspection.
2. Access and browse the Windows filesystem structure within the VHD.
3. Verify successful mount and extract relevant data without modifying the image.

## Instructions

### Step 1: Install libguestfs-tools

**Context**: Ensure the guestmount tool is available on the Linux system. This is a prerequisite for mounting VHD images.

If not already installed, use the package manager to install it.

```bash
sudo apt update && sudo apt install libguestfs-tools
```

> This command installs the necessary libraries and tools. Expected output includes package download and installation confirmation without errors.

### Step 2: Prepare the Mount Directory

**Context**: Create a clean directory to serve as the mount point for the VHD contents. This allows organized access to the files.

```bash
sudo mkdir -p /mnt/vhd_mount
```

> Expected output: The directory /mnt/vhd_mount is created if it does not exist. Verify with `ls /mnt` to see the new folder.

### Step 3: Mount the VHD Image

**Context**: Use guestmount to attach and mount the VHD file to the prepared directory in read-only mode.

**Command** ([[commands/guestmount-mount-vhd-file]]):
```bash
guestmount --add $_IMAGE.vhd --inspector --ro $_MOUNT_DIR
```

> The --add flag specifies the VHD file, --inspector auto-detects the filesystem, and --ro ensures read-only access. Replace $_IMAGE with the path to your VHD file (e.g., /path/to/image.vhd) and $_MOUNT_DIR with /mnt/vhd_mount. Expected output: No errors, and the mount completes silently or with a confirmation message. The VHD contents will be accessible at the mount directory.

### Step 4: Verify the Mount and Access Files

**Context**: Confirm the mount succeeded by listing the contents of the mounted directory.

```bash
ls -la $_MOUNT_DIR
```

> Expected output: A listing of the Windows filesystem root, such as directories like Windows, Users, Program Files. If empty or error, check permissions or VHD integrity.

### Step 5: Unmount When Finished

**Context**: Safely detach the VHD to free resources and prevent any lock issues.

```bash
guestunmount $_MOUNT_DIR
```

> Expected output: The mount is detached without errors. Verify with `ls /proc/mounts` to ensure the entry is gone.
