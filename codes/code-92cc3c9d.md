---
id: 92cc3c9d-b1fe-4143-9fbc-b3712f8bba63
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:28.626641+00:00'
updated_at: '2023-04-10T20:37:41.758952+00:00'
---

# Code Snippet 92cc3c9d

**Language**: Powershell

```powershell
net user
whoami /all
Get-LocalUser | ft Name,Enabled,LastLogon
Get-ChildItem C:\Users -Force | select Name
```


