---
id: c648129e-898e-4a1c-8a90-c3ea3f48be2a
name: check-sebackupprivilege-status
type: command
executor: powershell
data: Get-SeBackupPrivilege
output: null
created_at: '2023-04-06T03:56:06.525883+00:00'
updated_at: '2023-04-10T20:26:17.815665+00:00'
platforms:
  - Windows
tags:
  - privilege
  - escalation
verified: true
validated: true
---

# check-sebackupprivilege-status

## Command

```powershell
Get-SeBackupPrivilege
```

## Description

This command queries the current process for the status of the SeBackupPrivilege, which allows bypassing file security to read any file. Use it after enabling the privilege to verify activation in post-exploitation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; checks current process token | Yes |

## Examples

### Basic Usage

```powershell
Get-SeBackupPrivilege
```

## Expected Output

Status output indicating enabled or disabled, e.g., "SeBackupPrivilege: Enabled" or "SeBackupPrivilege: Disabled".

## Related

- [[procedures/Abusing-Backup-Operators-Group-for-Sensitive-File-Access]]
- [[commands/enable-sebackupprivilege]]
