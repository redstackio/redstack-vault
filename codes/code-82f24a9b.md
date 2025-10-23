---
id: 82f24a9b-a959-4fa7-ae3b-133490af95ae
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:02.228353+00:00'
updated_at: '2023-04-06T21:33:38.760126+00:00'
---

# Code Snippet 82f24a9b

**Language**: Powershell

```powershell
Get-DomainPolicy

#This command is used to retrieve the policy configurations of the Domain about system access or kerberos. The following commands can be used to get specific policy configurations:
(Get-DomainPolicy)."system access"
(Get-DomainPolicy)."kerberos policy"
```


