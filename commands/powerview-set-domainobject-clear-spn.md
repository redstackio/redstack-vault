---
type: command
executor: powershell
data: Set-DomainObject -Identity $_TARGET_USER -Clear serviceprincipalname
output: null
platforms:
  - Windows
tags:
  - active-directory
  - cleanup
verified: true
validated: true
---

# powerview-set-domainobject-clear-spn

## Command

```powershell
Set-DomainObject -Identity $_TARGET_USER -Clear serviceprincipalname
```

## Description

Clears the Service Principal Name from a user account after ticket extraction to restore the original state and reduce detection risk.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity | Target username or DN | Yes |
| -Clear | Property to clear (serviceprincipalname) | Yes |
| $_TARGET_USER | Target username | Yes |

## Examples

### Basic Usage

```powershell
Set-DomainObject -Identity targetuser -Clear serviceprincipalname
```

## Expected Output

Set-DomainObject function completed.

## Related

- [[procedures/Active-Directory-ACL-Abuse-via-Kerberoasting-and-AS-REP-Roasting]]
- [[tools/PowerView]]
