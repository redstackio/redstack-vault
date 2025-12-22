---
type: command
executor: powershell
data: >-
  Get-ADObject -Filter {TrustedForDelegation -eq $true} -Properties
  TrustedForDelegation | Select Name, ObjectClass, TrustedForDelegation
output: null
created_at: '2023-04-06T03:56:07.426068+00:00'
updated_at: '2023-04-10T20:36:05.043995+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - enumeration
verified: true
validated: true
---

# PowerShell-Check-TrustedForDelegation

## Command

```powershell
Get-ADObject -Filter {TrustedForDelegation -eq $true} -Properties TrustedForDelegation | Select Name, ObjectClass, TrustedForDelegation
```

## Description

This PowerShell command queries Active Directory for user or computer objects with the TrustedForDelegation attribute enabled, indicating unconstrained Kerberos delegation. It is used during reconnaissance to identify potential abuse targets in domain environments for credential theft techniques.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-Filter {TrustedForDelegation -eq $true}` | AD filter to match objects with unconstrained delegation enabled | Yes |
| `-Properties TrustedForDelegation` | Specifies the attribute to retrieve | Yes |
| `| Select Name, ObjectClass, TrustedForDelegation` | Formats output to show name, type (user/computer), and delegation status | Yes |

## Examples

### Basic Usage

```powershell
Get-ADObject -Filter {TrustedForDelegation -eq $true} -Properties TrustedForDelegation | Select Name, ObjectClass, TrustedForDelegation
```

### Advanced Usage (Users Only)

```powershell
Get-ADUser -Filter {TrustedForDelegation -eq $true} -Properties TrustedForDelegation | Select Name, TrustedForDelegation
```

## Expected Output

Name                  ObjectClass TrustedForDelegation
----                  ----------- --------------------- 
PRINTSERVER01         computer    True                  
DOMAINADMIN           user        True                  

This lists objects with delegation enabled, confirming potential for abuse.

## Related

- [[procedures/Kerberos-Unconstrained-Delegation-with-SpoolService-Abuse]]
