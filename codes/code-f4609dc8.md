---
id: f4609dc8-aa34-453e-bb49-f878e9df5110
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:04.401193+00:00'
updated_at: '2023-04-10T20:26:06.621624+00:00'
---

# Code Snippet f4609dc8

**Language**: Powershell

```powershell
enum4linux | grep -i desc

Get-WmiObject -Class Win32_UserAccount -Filter "Domain='COMPANYDOMAIN' AND Disabled='False'" | Select Name, Domain, Status, LocalAccount, AccountType, Lockout, PasswordRequired, PasswordChangeable, Description, SID
```
