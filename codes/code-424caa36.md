---
id: 424caa36-c295-477c-90d2-577a0dbd0972
type: code
language: Powershell
verified: false
created_at: '2023-05-28T03:59:38.555492+00:00'
updated_at: '2023-05-28T03:59:38.883973+00:00'
---

# Code Snippet 424caa36

**Language**: Powershell

```powershell
# adduser.ps1
$passwd = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force


New-LocalUser -Name user -Password $passwd 
Add-LocalGroupMember -Group Administrators -Member user
```


