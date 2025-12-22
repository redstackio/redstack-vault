---
id: a7cfb5c7-1984-4fba-9eae-bf033c28a572
name: icacls-view-file-permissions
type: command
executor: cmd
data: icacls $_FILE_PATH
output: null
created_at: '2023-04-06T03:56:28.851248+00:00'
updated_at: '2023-04-10T20:37:52.895105+00:00'
platforms:
  - Windows
tags:
  - permissions
  - recon
verified: true
validated: true
---

# icacls-view-file-permissions

## Command

```cmd
icacls $_FILE_PATH
```

## Description

Displays or modifies access control lists (ACLs) for files and folders on Windows. Use this to check permissions on sensitive files like the SAM registry hive to identify misconfigurations such as HiveNightmare.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILE_PATH | Path to the file or folder (e.g., C:\\Windows\\System32\\config\\SAM) | Yes |

## Examples

### Basic Usage

```cmd
icacls C:\Windows\System32\config\SAM
```

### Advanced Usage

```cmd
icacls C:\Windows\System32\config /save acl_backup.txt /t
```

## Expected Output

```
C:\Windows\System32\config\SAM BUILTIN\Administrators:(I)(F)
           NT AUTHORITY\SYSTEM:(I)(F)
           BUILTIN\Users:(I)(RX)
```

This shows full control for admins and system, but read access for users—indicating vulnerability.

## Related

- [[procedures/HiveNightmare-SAM-Dump-via-Shadow-Copies]]
