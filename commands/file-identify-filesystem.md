---
type: command
executor: bash
data: sudo file -s $_DEVICE_PATH
tags:
  - linux
  - filesystem
platforms:
  - Linux
verified: true
validated: true
---

# file-identify-filesystem

## Command

```bash
sudo file -s $_DEVICE_PATH
```

## Description

Determines the filesystem type of a block device or file, aiding in proper mounting of volumes like EBS snapshots.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s $_DEVICE_PATH | Special file or device path (e.g., /dev/xvda1) | Yes |

## Examples

### Basic Usage

```bash
sudo file -s /dev/xvda1
```

### Advanced Usage

For a specific device:

```bash
sudo file -s /dev/xvdf
```

## Expected Output

Output indicating type:

`/dev/xvda1: Linux rev 1.0 ext4 filesystem data, UUID=abcd-1234 (needs journal recovery)
`

## Related

- [[commands/mount-block-device]]
- [[procedures/AWS-Extract-EBS-Backup-to-EC2-Instance]]
