---
type: command
executor: bash
data: >-
  mount -t cifs //$_TARGET_IP/$_SHARE -o
  'username="",password="",vers=3.0,guest' /$_MOUNT_POINT
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - network
  - discovery
verified: true
validated: true
---

# mount-cifs-share-null-session

## Command

```bash
mount -t cifs //$_TARGET_IP/$_SHARE -o 'username="",password="",vers=3.0,guest' /$_MOUNT_POINT
```

## Description

This command mounts a remote Windows CIFS/SMB share anonymously (null session) on a Linux system. It attempts guest access without credentials, useful for enumerating exposed shares where null sessions are permitted.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the Windows target | Yes |
| $_SHARE | Name of the share (e.g., IPC$, PUBLIC) | Yes |
| $_MOUNT_POINT | Local directory to mount the share (must exist) | Yes |
| -t cifs | Specifies CIFS filesystem type | Built-in |
| -o | Options for mount (null creds and guest) | Built-in |
| vers=3.0 | SMB protocol version | Recommended |
| guest | Enables guest/anonymous access | Yes for null |

## Examples

### Basic Usage

```bash
mount -t cifs //192.168.1.100/IPC$ -o 'username="",password="",vers=3.0,guest' /mnt/ipc
```

### Advanced Usage

```bash
mount -t cifs //target.example.com/SHARE -o 'username="",password="",vers=2.1,guest,iocharset=utf8' /mnt/share
```

> Adds charset for file name handling.

## Expected Output

If successful (null session allowed):
```
```
(No password prompt). Verify with `ls /mnt/share`:
```
total 16
drwxr-xr-x 5 root root 0 Oct 1 12:00 .
drwxr-xr-x 3 root root 4096 Oct 1 12:00 ..
-rw-r--r-- 1 root root 0 Oct 1 12:00 file.txt
```
Failure: "mount error(127): The remote system refused the share" or similar.

## Related

- [[procedures/Mount-Windows-CIFS-Share]]
- [[commands/mount-cifs-share-with-credentials]]
