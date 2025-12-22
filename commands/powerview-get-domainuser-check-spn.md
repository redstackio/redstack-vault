---
type: command
executor: powershell
data: Get-DomainUser -Identity $_TARGET_USER | Select-Object serviceprincipalname
output: null
platforms:
  - Windows
tags:
  - active-directory
  - kerberoasting
verified: true
validated: true
---

# powerview-get-domainuser-check-spn

## Command

```powershell
Get-DomainUser -Identity $_TARGET_USER | Select-Object serviceprincipalname
```

## Description

Queries a specific domain user for existing Service Principal Names (SPNs) to determine if Kerberoasting is feasible or if an SPN needs to be set.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity | Username or SID of the target user | Yes |
| $_TARGET_USER | Placeholder for target username (e.g., targetuser) | Yes |

## Examples

### Basic Usage

```powershell
Get-DomainUser -Identity targetuser | Select-Object serviceprincipalname
```

## Expected Output

serviceprincipalname : {}

(Empty array if no SPN; otherwise lists SPNs like ops/service).

## Related

- [[procedures/Active-Directory-ACL-Abuse-via-Kerberoasting-and-AS-REP-Roasting]]
- [[tools/PowerView]]
