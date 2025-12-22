---
type: command
executor: bash
data: sudo mount $_DEVICE_PATH /mnt/backup
tags:
  - linux
  - mount
platforms:
  - Linux
verified: true
validated: true
---

# mount-block-device

## Command

```bash
sudo mount $_DEVICE_PATH /mnt/backup
```

## Description

Mounts a block device to a specified directory, making the filesystem accessible for reading files from backups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DEVICE_PATH | Path to the device (e.g., /dev/xvdf) | Yes |
| /mnt/backup | Mount point directory (create if needed) | Yes |

## Examples

### Basic Usage

```bash
sudo mount /dev/xvdf /mnt/backup
```

### Advanced Usage

With filesystem type:

```bash
sudo mount -t ext4 /dev/xvdf /mnt/backup
```

## Expected Output

No output on success; verify with `df -h` or `ls /mnt/backup` showing mounted contents.

## Related

- [[commands/file-identify-filesystem]]
- [[procedures/AWS-Extract-EBS-Backup-to-EC2-Instance]]
