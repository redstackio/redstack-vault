---
id: 92cc3c9d-b1fe-4143-9fbc-b3712f8bba63
name: enumerate-local-users-powershell
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:28.626641+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - users
validated: true
---

# enumerate-local-users-powershell

## Code

```powershell
net user
whoami /all
Get-LocalUser | ft Name,Enabled,LastLogon
Get-ChildItem C:\Users -Force | select Name
```

## Description

This PowerShell script enumerates all local users using a mix of net, whoami, and Get-LocalUser cmdlets, plus lists user profile directories. It provides a comprehensive view of user accounts, statuses, and existence on disk for identifying targets in enumeration.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (none) | No variables; runs on local system | N/A |

## Usage

Paste into PowerShell on a Windows target during initial foothold to map users. Use output to select targets for password spraying or privilege checks. Ideal after initial access via RDP or shell.

## Detection

- PowerShell execution logging (ModuleLogging, ScriptBlockLogging) captures Get-LocalUser and net user
- File access to C:\Users monitored by FS auditing
- EDR alerts on whoami /all as it's verbose

## Related

- [[procedures/windows-user-enumeration-and-privilege-check]]
- [[commands/net-user-list-all]]
