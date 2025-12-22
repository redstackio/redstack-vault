---
type: command
executor: bash
data: rpcclient -U 'DOMAIN\username%password' //TARGET_IP -c 'lookupnames username'
output: null
created_at: '2023-04-06T03:56:02.621840+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - sid-resolution
verified: true
validated: true
---

# lookup-user-sid-with-rpcclient

## Command

```bash
rpcclient -U 'DOMAIN\username%password' //TARGET_IP -c 'lookupnames username'
```

## Description

This command uses Samba's rpcclient to connect to a Windows target's IPC$ share and query the Security Account Manager (SAMR) for a user's Security Identifier (SID) by username. It is useful for remote enumeration in Active Directory without local access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -U 'DOMAIN\username%password' | Credentials for authentication (domain\user:pass) | Yes |
| //TARGET_IP | Target host IP or hostname | Yes |
| -c 'lookupnames username' | RPC command to execute: lookupnames followed by the target username | Yes |

## Examples

### Basic Usage

```bash
rpcclient -U 'LAB\lambda%P@ssw0rd' //10.10.10.10 -c 'lookupnames lambda'
```

### Advanced Usage

For multiple users, chain commands or script iterations.

## Expected Output

```
john.smith S-1-5-21-2923581646-3335815371-2872905324-1107 (User: 1)
```

The output shows the username, SID, and user type (User: 1).

## Related

- [[Related Procedure: Exploit-MS14-068-Kerberos-Checksum-Validation-for-AD-Privilege-Escalation]]
- [[commands/get-user-accounts-with-wmic]]
