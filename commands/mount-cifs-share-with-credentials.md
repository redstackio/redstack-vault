---
type: command
executor: bash
data: >-
  mount -t cifs //$_TARGET_IP/$_SHARE -o
  'username="$_USERNAME",password="$_PASSWORD",vers=3.0' /$_MOUNT_POINT
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

# mount-cifs-share-with-credentials

## Command

```bash
mount -t cifs //$_TARGET_IP/$_SHARE -o 'username="$_USERNAME",password="$_PASSWORD",vers=3.0' /$_MOUNT_POINT
```

## Description

This command mounts a remote Windows CIFS/SMB share on a Linux system using provided credentials. It attaches the share to a local mount point, allowing file access as a local directory. Use this when authenticated access is required for protected shares.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the Windows target | Yes |
| $_SHARE | Name of the share (e.g., IPC$, ADMIN$) | Yes |
| $_USERNAME | Username for authentication | Yes |
| $_PASSWORD | Password for the username | Yes |
| $_MOUNT_POINT | Local directory to mount the share (must exist) | Yes |
| -t cifs | Specifies CIFS filesystem type | Built-in |
| -o | Options for mount (credentials and version) | Built-in |
| vers=3.0 | SMB protocol version (use 2.1 or 1.0 for legacy) | Recommended |

## Examples

### Basic Usage

```bash
mount -t cifs //192.168.1.100/C$ -o 'username="admin",password="pass123",vers=3.0' /mnt/share
```

### Advanced Usage

```bash
mount -t cifs //target.example.com/IPC$ -o 'username="guest",password="",vers=3.0,uid=1000,gid=1000' /mnt/ipc
```

> Adds uid/gid for ownership mapping.

## Expected Output

Successful mount shows:
```
Password for admin@//192.168.1.100: 
(enter password)
```
Followed by no error messages. Verify with `df -h` listing the mount, or `ls /mnt/share` showing share files like:
```
total 0
drwxr-xr-x 2 root root 0 Oct 1 12:00 .
drwxr-xr-x 3 root root 4096 Oct 1 12:00 ..
```
Errors include "mount error(13): Permission denied" for bad creds.

## Related

- [[procedures/Mount-Windows-CIFS-Share]]
- [[commands/mount-cifs-share-null-session]]
