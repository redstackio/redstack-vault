---
id: ef79900d-8426-405d-bc5f-05c858c7c5c6
name: ls-list-temp-dir-files
type: command
executor: bash
data: ls $_RPATH_DIR
output: null
created_at: '2023-04-06T03:56:19.401575+00:00'
updated_at: '2023-04-10T20:34:31.017246+00:00'
platforms:
  - Linux
tags:
  - recon
  - linux
verified: true
validated: true
---

# ls-list-temp-dir-files

## Command

```bash
ls $_RPATH_DIR
```

## Description

Lists files in the RPATH directory to verify writability and presence of placed libraries before and after copying/modifying.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_RPATH_DIR | Path to the RPATH directory (e.g., /var/tmp/flag15) | Yes |

## Examples

### Basic Usage

```bash
ls /var/tmp/flag15
```

### Advanced Usage

```bash
ls -la /tmp
```

## Expected Output

```
libc.so.6
```

## Related

- [[procedures/Linux-Privilege-Escalation-via-Shared-Library-RPATH-Hijacking]]
- [[commands/cp-copy-libc-to-temp-dir]]
