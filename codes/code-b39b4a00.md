---
id: b39b4a00-3a01-4576-96d1-4e9a97fc9f11
type: code
language: Powershell
verified: false
created_at: '2023-05-25T04:25:16.411644+00:00'
updated_at: '2023-05-25T04:38:04.303435+00:00'
---

# Code Snippet b39b4a00

**Language**: Powershell

```powershell
# adduser.ps1
$passwd = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force

New-LocalUser -Name studentX -Password $passwd 
Add-LocalGroupMember -Group Administrators -Member studentX
```
