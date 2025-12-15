---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: 'icacls "C:\\Program Files\\Ubiquiti UniFi Video"'
tags:
  - permissions
  - audit
type: command
output: >-
  Directory permissions displayed, e.g., Users:(OI)(CI)(F) indicating full
  control.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:44.489Z'
verified: false
validated: true
submitted: true
---
# icacls-check-perms

## Command

```cmd
icacls "C:\Program Files\Ubiquiti UniFi Video"
```

## Description

Displays the Access Control Lists (ACLs) for the specified directory, revealing if unprivileged users have write/modify permissions. Use this to audit insecure default settings in software installations like UniFi Video.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Path | Target directory (e.g., installation folder) | Yes |

## Examples

### Basic Usage

```cmd
icacls "C:\Program Files\Ubiquiti UniFi Video"
```

### Advanced Usage

```cmd
icacls "C:\Program Files\Ubiquiti UniFi Video" /save acl_backup.txt /t
```

## Expected Output

Processed file: C:\Program Files\Ubiquiti UniFi Video
Successfully processed 1 files; Failed processing 0 files
Users:(OI)(CI)(F)
BUILTIN\Administrators:(I)(OI)(CI)(F)

Indicates full control (F) for Users group.

## Related

- [[Related Procedure|procedures/Exploit-Weak-ACLs-in-UniFi-Video-Directory]]
