---
id: ad029fc2-cd21-428c-a150-2628209da72d
name: mkdir-create-mount-point
type: command
executor: bash
data: mkdir $_MOUNT_POINT
output: null
created_at: '2023-04-06T03:56:19.323075+00:00'
updated_at: '2023-04-10T20:34:35.902057+00:00'
platforms:
  - Linux
tags:
  - nfs
  - filesystem
verified: true
validated: true
---

# mkdir-create-mount-point

## Command

```bash
mkdir $_MOUNT_POINT
```

## Description

This command creates a new directory on the local filesystem to use as a mount point for an NFS share. It is a prerequisite for mounting remote shares.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MOUNT_POINT | Path for the new directory (e.g., /tmp/nfsdir) | Yes |

## Examples

### Basic Usage

```bash
mkdir /tmp/nfsdir
```

### Advanced Usage

```bash
mkdir -p /tmp/mount/nfs
```

## Expected Output

```
(Silent if successful; use ls to verify the directory exists)
```

Error like "File exists" if directory already present.

## Related

- [[procedures/Linux-Privilege-Escalation-via-NFS-Root-Squashing]]
