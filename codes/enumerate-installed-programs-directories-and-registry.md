---
type: code
language: powershell
verified: true
platforms:
  - Windows
tags:
  - enumeration
  - installed-software
validated: true
---

# enumerate-installed-programs-directories-and-registry

## Code

```powershell
Get-ChildItem 'C:\Program Files', 'C:\Program Files (x86)' | ft Parent,Name,LastWriteTime
Get-ChildItem -path Registry::HKEY_LOCAL_MACHINE\SOFTWARE | ft Name
```

## Description

PowerShell code to list installed programs by scanning Program Files directories and HKLM\SOFTWARE registry keys, helping identify vulnerable software or writable install paths for escalation via binary replacement.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No variables; fixed paths | N/A |

## Usage

Run in PowerShell to output tables of directories and registry entries. Follow up with icacls on listed paths to check permissions for potential DLL hijacking or service abuse.

## Detection

- File system access logs if monitored (e.g., via Sysmon Event ID 11 for directory listings).
- Registry queries in Security Event Log (Event ID 4657 for HKLM access).
- PowerShell cmdlets like Get-ChildItem in transcription logs.

## Related

- [[procedures/windows-processes-and-tasks-enumeration-for-privilege-escalation]]
