---
id: 23a35706-cba1-4bd2-9dd2-1288c13278a8
name: mount-device-to-directory
type: command
executor: bash
data: sudo mount $_DEVICE $_MOUNT_POINT
output: null
created_at: '2023-04-06T03:56:13.852161+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - storage
  - aws
  - mount
verified: true
validated: true
---

# mount-device-to-directory

## Command

```bash
sudo mount $_DEVICE $_MOUNT_POINT
```

## Description

Mounts a block device like an EBS volume to a specified directory, making its filesystem accessible for read/write operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DEVICE | Path to the device (e.g., /dev/xvdf) | Yes |
| $_MOUNT_POINT | Target directory (e.g., /opt/persistent-data) | Yes |
| sudo | Run with root privileges | Yes |

## Examples

### Basic Usage

```bash
sudo mount /dev/xvdf /opt/persistent-data
```

### Advanced Usage

```bash
sudo mount -o defaults,nofail /dev/xvdf /opt/persistent-data
```

## Expected Output

No output on success, or error if device not found/invalid. Verify with 'mount | grep $_MOUNT_POINT' showing /dev/xvdf on /opt/persistent-data type ext4.

## Related

- [[procedures/Mount-EBS-Volume-to-Directory-for-Persistence]]
