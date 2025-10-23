---
id: 6e9d570b-0115-4678-b519-f35a1de8ff80
type: code
language: Powershell
verified: false
created_at: '2023-05-25T04:38:04.036768+00:00'
updated_at: '2023-05-28T03:59:38.582887+00:00'
---

# Code Snippet 6e9d570b

**Language**: Powershell

```powershell
# adduser.ps1
$passwd = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force


New-LocalUser -Name studentX -Password $passwd 
Add-LocalGroupMember -Group Administrators -Member studentX
```


