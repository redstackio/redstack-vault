---
id: 22f6fdfb-35b7-4217-a312-5433d75893b5
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:28.627017+00:00'
updated_at: '2023-04-10T20:37:41.758952+00:00'
---

# Code Snippet 22f6fdfb

**Language**: Powershell

```powershell
net localgroup administrators
Get-LocalGroupMember Administrators | ft Name, PrincipalSource
Get-LocalGroupMember Administrateurs | ft Name, PrincipalSource
```


