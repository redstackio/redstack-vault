---
id: 1f12e2e6-115f-469c-8d11-e7dbe5738cdb
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:06.961679+00:00'
updated_at: '2023-04-10T20:26:00.825161+00:00'
---

# Code Snippet 1f12e2e6

**Language**: Powershell

```powershell
# Save the blob to a variable
$gmsa = Get-ADServiceAccount -Identity 'SQL_HQ_Primary' -Properties 'msDS-ManagedPassword'
$mp = $gmsa.'msDS-ManagedPassword'

# Decode the data structure using the DSInternals module
ConvertFrom-ADManagedPasswordBlob $mp
```
