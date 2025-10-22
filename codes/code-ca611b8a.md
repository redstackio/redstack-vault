---
id: ca611b8a-1966-4dc7-bbe5-f75935fc5ac1
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:04.557193+00:00'
updated_at: '2023-04-10T20:26:38.835543+00:00'
---

# Code Snippet ca611b8a

**Language**: ps1

```ps1
$gmsa =  Get-ADServiceAccount -Identity 'SVC_SERVICE_ACCOUNT' -Properties 'msDS-ManagedPassword'
$blob = $gmsa.'msDS-ManagedPassword'
$mp = ConvertFrom-ADManagedPasswordBlob $blob
$hash1 =  ConvertTo-NTHash -Password $mp.SecureCurrentPassword
```
