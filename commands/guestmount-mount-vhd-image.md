---
id: 40c17768-34cb-40ad-8f18-a0bd1018a52e
name: guestmount-mount-vhd-image
type: command
executor: bash
data: guestmount --add $_IMAGE --inspector --ro $_MOUNT_DIR
output: null
created_at: '2019-10-11T22:11:00.200134+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - mounting
  - vhd
  - forensics
verified: true
validated: true
---

# guestmount-mount-vhd-image

## Command

```bash
guestmount --add $_IMAGE --inspector --ro $_MOUNT_DIR
```

## Description

This command mounts a Windows VHD (Virtual Hard Disk) file on a Linux system using guestmount from the libguestfs toolkit. It attaches the virtual disk image and exposes its filesystem in read-only mode at the specified mount directory, making it ideal for forensic analysis or secure inspection without modifying the original data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_IMAGE | Path to the VHD file (e.g., /path/to/disk.vhd) | Yes |
| --inspector | Automatically detect and mount filesystems inside the image | Yes |
| --ro | Mount in read-only mode to preserve data integrity | Yes |
| $_MOUNT_DIR | Target directory to mount the image contents (must exist and be empty) | Yes |

## Examples

### Basic Usage

```bash
guestmount --add /home/user/image.vhd --inspector --ro /mnt/vhd
```

### Advanced Usage

For a specific partition if automatic detection fails:

```bash
guestmount --add /home/user/image.vhd --ro -i /dev/sdb1 /mnt/vhd
```

## Expected Output

The command typically produces minimal output on success, silently mounting the filesystem. You can verify the mount with `mount | grep vhd` or by listing files in $_MOUNT_DIR. Errors may include messages like "libguestfs: error: could not read image" if the VHD is corrupted or inaccessible.

## Related

- [[tools/guestmount]]
- [[procedures/Mount-Windows-VHD-Image-on-Linux]]
