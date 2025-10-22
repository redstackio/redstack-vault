---
id: af28ade0-efd2-4313-973b-cbd67306d322
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:29.377506+00:00'
updated_at: '2023-04-10T20:37:39.718796+00:00'
---

# Code Snippet af28ade0

**Language**: Powershell

```powershell
tasklist /v
net start
sc query
Get-Service
Get-Process
Get-WmiObject -Query "Select * from Win32_Process" | where {$_.Name -notlike "svchost*"} | Select Name, Handle, @{Label="Owner";Expression={$_.GetOwner().User}} | ft -AutoSize
```
