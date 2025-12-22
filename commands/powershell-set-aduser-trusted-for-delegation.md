---
type: command
executor: powershell
data: Set-ADUser -Identity 'User1' -TrustedForDelegation $true
tags:
  - active-directory
  - delegation
platforms:
  - Windows
verified: true
validated: true
---

# powershell-set-aduser-trusted-for-delegation

## Command

```powershell
Set-ADUser -Identity $_USERNAME -TrustedForDelegation $true
```

## Description

Enables unconstrained Kerberos delegation on a domain user account, allowing it to impersonate users to any service. Use this in delegation abuse scenarios like Bronze Bit to prepare accounts for ticket forwarding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity $_USERNAME | Username to modify (e.g., User1) | Yes |
| -TrustedForDelegation $true | Enables delegation trust | Yes |

## Examples

### Basic Usage

```powershell
Set-ADUser -Identity 'User1' -TrustedForDelegation $true
```

### Verification

```powershell
Get-ADUser -Identity 'User1' -Properties TrustedForDelegation
```

## Expected Output

No output on success; the user account's TrustedForDelegation property is set to True. Errors if insufficient permissions.

## Related

- [[procedures/Kerberos-Bronze-Bit-Attack]]
- [[commands/powershell-set-aduser-service-principal-names]]
