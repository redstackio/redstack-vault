---
id: 3ba2c2d8-c161-4ca6-a67b-97de3a4e33cc
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:31.313428+00:00'
updated_at: '2023-04-10T20:37:57.585269+00:00'
---

# Code Snippet 3ba2c2d8

**Language**: Powershell

```powershell
PS C:\> PsExec.exe  \\srv01.domain.local -u DOMAIN\username -p password cmd.exe

# switch admin user to NT Authority/System
PS C:\> PsExec.exe  \\srv01.domain.local -u DOMAIN\username -p password cmd.exe -s 
```
