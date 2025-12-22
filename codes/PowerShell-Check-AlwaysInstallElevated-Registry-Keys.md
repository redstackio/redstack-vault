---
id: 7e4b4635-8aac-49b6-96a6-f33aa29b84df
name: PowerShell-Check-AlwaysInstallElevated-Registry-Keys
type: code
language: powershell
verified: true
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - registry
  - privesc
  - powershell
validated: true
---

# PowerShell-Check-AlwaysInstallElevated-Registry-Keys

## Code

```powershell
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

Get-ItemProperty HKLM:\Software\Policies\Microsoft\Windows\Installer
Get-ItemProperty HKCU:\Software\Policies\Microsoft\Windows\Installer
```

## Description

This PowerShell script checks the AlwaysInstallElevated registry values in both HKCU and HKLM hives to determine if the system is vulnerable to MSI-based privilege escalation. It combines cmd-compatible reg query for direct value retrieval and PowerShell's Get-ItemProperty for full key inspection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; runs as-is | N/A |

## Usage

Execute in a PowerShell terminal on the target Windows system during reconnaissance for AlwaysInstallElevated exploitation. Use before attempting to set or exploit the keys in privilege escalation procedures.

## Detection

- PowerShell execution logging (Module Logging, Script Block Logging) will capture the reg query and Get-ItemProperty calls.
- Sysmon Event ID 1 (Process Creation) for powershell.exe spawning cmd.exe implicitly.
- Anomalous registry reads on Installer policy keys.

## Related

- [[procedures/Windows-AlwaysInstallElevated-Privilege-Escalation]]
