---
id: c69b5a01-7999-4232-8b4d-4408877474f0
type: code
language: Powershell
verified: false
created_at: '2023-05-25T04:23:14.560676+00:00'
updated_at: '2023-05-25T04:24:43.307218+00:00'
---

# Code Snippet c69b5a01

**Language**: Powershell

```powershell
# adduser.ps1
$passwd = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force


New-LocalUser -Name studentX -Password $passwd 
Add-LocalGroupMember -Group Administrators -Member studentX
```


