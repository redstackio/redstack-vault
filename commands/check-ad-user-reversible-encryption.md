---
id: 7cde5c5d-f51d-40d5-9208-8a6136ed4e74
name: check-ad-user-reversible-encryption
type: command
executor: powershell
data: >-
  Get-ADUser -Filter * -Properties UserFlags | Where-Object { ($_.UserFlags
  -band 0x80) -eq 0x80 } | Select Name, UserFlags
output: null
created_at: '2023-04-06T03:56:04.127172+00:00'
updated_at: '2023-04-10T20:35:59.250955+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - credential-access
verified: true
validated: true
---

# check-ad-user-reversible-encryption

## Command

```powershell
Get-ADUser -Filter * -Properties UserFlags | Where-Object { ($_.UserFlags -band 0x80) -eq 0x80 } | Select Name, UserFlags
```

## Description

This PowerShell command queries all AD user accounts for the UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED flag (0x80), indicating reversible password encryption is enabled. Use it as a reconnaissance step before attempting NTDS dumps to confirm the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Filter * | Queries all users (can be narrowed, e.g., -Filter "Name -like 'admin*'" ) | Yes |
| -Properties UserFlags | Retrieves the UserFlags attribute for flag checking | Yes |
| Where-Object { ($_.UserFlags -band 0x80) -eq 0x80 } | Bitwise check for reversible encryption flag | Built-in |
| Select Name, UserFlags | Outputs user name and flags for review | Built-in |

## Examples

### Basic Usage

```powershell
Get-ADUser -Filter * -Properties UserFlags | Where-Object { ($_.UserFlags -band 0x80) -eq 0x80 } | Select Name, UserFlags
```

### Advanced Usage

```powershell
Get-ADUser -Filter "Enabled -eq 'True'" -Properties UserFlags | Where-Object { ($_.UserFlags -band 0x80) -eq 0x80 } | Select Name, UserFlags, DistinguishedName
```
Narrow to enabled users and add DN for context.

## Expected Output

```
Name                    UserFlags
----                    ----------
TestUser                54480
AdminAccount            54480
```
Lists users with the flag set (UserFlags decimal value including 0x80). Empty output means no vulnerable accounts.

## Related

- [[procedures/Dump-AD-Domain-Credentials-via-NTDS-Reversible-Encryption]]
- [[techniques/Credential Dumping|T1003]]
