---
id: 9c3bccf2-0535-41c7-9276-ad506eae57be
name: powershell-get-authenticodesignature-laps-admpwd-dll
type: command
executor: powershell
data: 'Get-AuthenticodeSignature ''C:\Program Files\LAPS\CSE\Admpwd.dll'''
output: null
created_at: '2023-04-06T03:56:04.492783+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - laps
  - active-directory
  - integrity-check
verified: true
validated: true
---

# powershell-get-authenticodesignature-laps-admpwd-dll

## Command

```powershell
Get-AuthenticodeSignature 'C:\Program Files\LAPS\CSE\Admpwd.dll'
```

## Description

This command retrieves the digital signature details for Admpwd.dll, confirming it is authentically signed by Microsoft to detect tampering or unsigned variants.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'C:\\Program Files\\LAPS\\CSE\\Admpwd.dll'` | Path to the Admpwd.dll file | Yes |

## Examples

### Basic Usage

```powershell
Get-AuthenticodeSignature 'C:\Program Files\LAPS\CSE\Admpwd.dll'
```

### Check Specific Signer

```powershell
(Get-AuthenticodeSignature 'C:\Program Files\LAPS\CSE\Admpwd.dll').Signer.Certificate.Subject
```

## Expected Output

    SignerCertificate                             Status                                           Path
    -----------------                             ------                                           ----
    [Subject] CN=Microsoft Code Signing PCA 2011... Valid                                            C:\Program Files\LAPS\CSE\Admpwd.dll

Status should be 'Valid' with Microsoft as signer.

## Related

- [[procedures/Check-LAPS-Installation-and-Retrieve-Password]]
- [[commands/powershell-get-filehash-laps-admpwd-dll]]
