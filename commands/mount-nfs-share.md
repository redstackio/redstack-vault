---
id: 23af707d-5a6a-410d-bd93-b467f00c9f41
name: mount-nfs-share
type: command
executor: bash
data: 'mount -t nfs $_SERVER_IP:$_SHARE_PATH $_MOUNT_POINT'
output: null
created_at: '2023-04-06T03:56:19.323159+00:00'
updated_at: '2023-04-10T20:34:35.902057+00:00'
platforms:
  - Linux
tags:
  - nfs
  - mount
verified: true
validated: true
---

# mount-nfs-share

## Command

```bash
mount -t nfs $_SERVER_IP:$_SHARE_PATH $_MOUNT_POINT
```

## Description

This command mounts a remote NFS share to a local directory, allowing access to the server's filesystem. Use it to attach vulnerable shares for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SERVER_IP | IP address of the NFS server | Yes |
| $_SHARE_PATH | Exported path on server (e.g., /shared) | Yes |
| $_MOUNT_POINT | Local directory to mount to | Yes |
| -t nfs | Specify NFS filesystem type | Yes |

## Examples

### Basic Usage

```bash
mount -t nfs 10.10.10.10:/shared /tmp/nfsdir
```

### Advanced Usage

```bash
mount -t nfs -o vers=3 10.10.10.10:/shared /tmp/nfsdir
```

## Expected Output

```
(Silent if successful; verify with df -h or ls $_MOUNT_POINT)
```

Errors: "mount.nfs: Connection timed out" (network issue) or "access denied by server" (permission denied).

## Related

- [[procedures/Linux-Privilege-Escalation-via-NFS-Root-Squashing]]
