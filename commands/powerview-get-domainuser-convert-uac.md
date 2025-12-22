---
type: command
executor: powershell
data: Get-DomainUser $_TARGET_USER | ConvertFrom-UACValue
output: null
platforms:
  - Windows
tags:
  - active-directory
  - as-rep-roasting
verified: true
validated: true
---

# powerview-get-domainuser-convert-uac

## Command

```powershell
Get-DomainUser $_TARGET_USER | ConvertFrom-UACValue
```

## Description

Retrieves a domain user's userAccountControl attribute and converts it to human-readable flags, useful for verifying pre-authentication status before/after modification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_USER | Target username | Yes |

## Examples

### Basic Usage

```powershell
Get-DomainUser targetuser | ConvertFrom-UACValue
```

## Expected Output

samaccountname     : targetuser
useraccountcontrol : 512
AccountDisabled    : False
DontReqPreAuth     : False

## Related

- [[procedures/Active-Directory-ACL-Abuse-via-Kerberoasting-and-AS-REP-Roasting]]
- [[tools/PowerView]]
