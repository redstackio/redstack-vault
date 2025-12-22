---
type: command
executor: powershell
data: >-
  Set-ADUser -Identity 'User1' -ServicePrincipalNames 'http/Server1.domain.com',
  'http/Server2.domain.com'
tags:
  - active-directory
  - spn
platforms:
  - Windows
verified: true
validated: true
---

# powershell-set-aduser-service-principal-names

## Command

```powershell
Set-ADUser -Identity $_USERNAME -ServicePrincipalNames $_SPN1, $_SPN2
```

## Description

Adds Service Principal Names (SPNs) to a user account, enabling Kerberos authentication for specific services. Critical for targeting services in delegation attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity $_USERNAME | Target username | Yes |
| -ServicePrincipalNames $_SPN_LIST | Comma-separated SPNs (e.g., cifs/Service2.test.local) | Yes |

## Examples

### Basic Usage

```powershell
Set-ADUser -Identity 'User1' -ServicePrincipalNames 'cifs/Service2.test.local'
```

## Expected Output

Success with no output; SPNs added to the account.

## Related

- [[procedures/Kerberos-Bronze-Bit-Attack]]
- [[commands/powershell-set-aduser-trusted-for-delegation]]
