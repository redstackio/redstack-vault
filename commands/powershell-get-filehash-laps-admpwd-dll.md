---
id: cd5dc006-8fc2-4491-bc8b-8fec0dfd184b
name: powershell-get-filehash-laps-admpwd-dll
type: command
executor: powershell
data: 'Get-FileHash ''C:\Program Files\LAPS\CSE\Admpwd.dll'''
output: null
created_at: '2023-04-06T03:56:04.492710+00:00'
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

# powershell-get-filehash-laps-admpwd-dll

## Command

```powershell
Get-FileHash 'C:\Program Files\LAPS\CSE\Admpwd.dll'
```

## Description

This command computes the SHA256 hash of the Admpwd.dll file to verify its integrity against known good values, ensuring the LAPS component has not been altered.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'C:\\Program Files\\LAPS\\CSE\\Admpwd.dll'` | Path to the Admpwd.dll file | Yes |
| `-Algorithm` | Hash algorithm (default: SHA256) | No |

## Examples

### Basic Usage

```powershell
Get-FileHash 'C:\Program Files\LAPS\CSE\Admpwd.dll'
```

### Specify Algorithm

```powershell
Get-FileHash 'C:\Program Files\LAPS\CSE\Admpwd.dll' -Algorithm SHA1
```

## Expected Output

    Algorithm       Hash                                                                   Path
    ---------       ----                                                                   ----
    SHA256          A1B2C3D4E5F6789012345678901234567890ABCDEF1234567890ABCDEF1234567     C:\Program Files\LAPS\CSE\Admpwd.dll

Compare hash to official Microsoft value for the DLL version.

## Related

- [[procedures/Check-LAPS-Installation-and-Retrieve-Password]]
- [[commands/powershell-get-childitem-laps-admpwd-dll]]
