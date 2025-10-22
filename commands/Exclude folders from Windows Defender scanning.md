---
id: ae368eea-e0d0-433b-9191-53f0d52d400c
name: Exclude folders from Windows Defender scanning
type: command
executor: bash
data: 'Add-MpPreference -ExclusionPath "C:\Temp"

  Add-MpPreference -ExclusionPath "C:\Windows\Tasks"

  Set-MpPreference -ExclusionProcess "word.exe", "vmwp.exe"'
output: null
created_at: '2023-04-06T03:56:26.616599+00:00'
updated_at: '2023-04-10T20:37:03.357263+00:00'
---

# Exclude folders from Windows Defender scanning

```bash
Add-MpPreference -ExclusionPath "C:\Temp"
Add-MpPreference -ExclusionPath "C:\Windows\Tasks"
Set-MpPreference -ExclusionProcess "word.exe", "vmwp.exe"
```
