---
id: 045d9046-9c91-4493-a88c-14808b4a3caf
type: command
executor: bash
data: mount /dev/mapper/$_CRYPT $_MOUNT_POINT
output: mount /dev/mapper/crypt-home /mnt/
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - filesystem
  - mount
verified: true
validated: true
---

# mount-filesystem-to-mount-point

## Command

```bash
mount /dev/mapper/$_CRYPT $_MOUNT_POINT
```

## Description

This command mounts an unlocked LUKS-encrypted file system (mapped via cryptsetup to /dev/mapper/) to a specified directory, allowing access to the decrypted contents. It is useful in post-exploitation scenarios for reading or extracting data from encrypted partitions after brute-forcing or decrypting the volume. The file system type is auto-detected; use -t if needed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_CRYPT` | Name of the LUKS mapper device (e.g., crypt-home) | Yes |
| `$_MOUNT_POINT` | Target directory path (must exist and be empty) | Yes |
| `-t FSTYPE` | Specify file system type (e.g., ext4, ntfs) | No (auto-detect) |
| `-o OPTIONS` | Mount options (e.g., ro for read-only, noexec) | No |

## Examples

### Basic Usage

```bash
sudo mount /dev/mapper/crypt-home /mnt/data
```

### Advanced Usage

Mount as read-only ext4:

```bash
sudo mount -t ext4 -o ro /dev/mapper/crypt-home /mnt/data
```

## Expected Output

On success, the command typically produces no output (silent). Verify the mount with:

```bash
df -h | grep $_MOUNT_POINT
ls $_MOUNT_POINT
```

Example verification output:

```
Filesystem                Size  Used Avail Use% Mounted on
/dev/mapper/crypt-home    50G   20G   30G  40% /mnt/data
```

Contents of /mnt/data will now be accessible, showing decrypted files.

## Related

- [[tools/mount]]
- [[procedures/Brute-Force-and-Mount-LUKS1-Encrypted-Filesystem]] (if applicable in context)
