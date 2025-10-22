---
id: 12b4c572-c0f6-49e7-942e-febc713287b8
name: Disable Windows Defender scanning
type: command
executor: bash
data: 'Set-MpPreference -DisableRealtimeMonitoring $true; Get-MpComputerStatus

  Set-MpPreference -DisableIOAVProtection $true

  Set-MpPreference -DisableScriptScanning 1'
output: null
created_at: '2023-04-06T03:56:26.616564+00:00'
updated_at: '2023-04-10T20:37:03.357263+00:00'
---

# Disable Windows Defender scanning

```bash
Set-MpPreference -DisableRealtimeMonitoring $true; Get-MpComputerStatus
Set-MpPreference -DisableIOAVProtection $true
Set-MpPreference -DisableScriptScanning 1
```
