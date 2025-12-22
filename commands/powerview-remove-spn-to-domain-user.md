---
id: 613ec3d3-fe39-4e2d-99e3-2b218aea3058
name: powerview-remove-spn-to-domain-user
type: command
executor: powershell
data: >-
  Set-DomainObject -Credential $Cred -Identity $_TARGET_USER -Clear
  serviceprincipalname
output: >-
  PS C:\Users\dave\Documents> Set-DomainObject -Credential $Cred -Identity steve
  -Clear serviceprincipalname


  Object modified successfully.
created_at: '2020-06-25T20:16:48.076258+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - powerview
  - active-directory
  - cleanup
verified: true
validated: true
---

# powerview-remove-spn-to-domain-user

## Command

```powershell
Set-DomainObject -Credential $Cred -Identity $_TARGET_USER -Clear serviceprincipalname
```

## Description

This PowerView command removes the Service Principal Name (SPN) attribute from an Active Directory user object to clean up after a Kerberoasting operation. It authenticates with provided credentials and clears the servicePrincipalName property.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Credential $Cred | PSCredential object for authentication | Yes |
| -Identity $_TARGET_USER | The target user account name | Yes |
| -Clear serviceprincipalname | Clears the specified attribute (servicePrincipalName) | Yes |

## Examples

### Basic Usage

```powershell
Set-DomainObject -Credential $Cred -Identity steve -Clear serviceprincipalname
```

### Advanced Usage

Clear multiple attributes if needed:

```powershell
Set-DomainObject -Credential $Cred -Identity steve -Clear serviceprincipalname,description
```

## Expected Output

Confirmation of the modification:

```
PS C:\Users\dave\Documents> Set-DomainObject -Credential $Cred -Identity steve -Clear serviceprincipalname

Object modified successfully.
```

## Related

- [[procedures/Add-SPN-to-Domain-User-and-Kerberoast-for-NTLMv2-Hash]]
- [[tools/PowerView]]
