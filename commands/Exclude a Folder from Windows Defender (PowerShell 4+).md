---
id: e4a2da5b-0c80-4cea-baf3-5a220578c3e7
name: Exclude a Folder from Windows Defender (PowerShell 4+)
type: command
executor: powershell
data: Add-MpPreference -ExclusionPath "$_PATH"
output: PS C:\> Add-MpPreference -ExclusionPath "C:\Windows\System32\spool\drivers\color"
created_at: '2020-03-04T18:38:21.956539+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Exclude a Folder from Windows Defender (PowerShell 4+)

```powershell
Add-MpPreference -ExclusionPath "$_PATH"
```

## Expected Output

```
PS C:\> Add-MpPreference -ExclusionPath "C:\Windows\System32\spool\drivers\color"
```


