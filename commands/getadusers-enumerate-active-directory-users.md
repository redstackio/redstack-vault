---
id: fb6ad137-2f98-48ff-b799-d84df4f4e934
name: getadusers-enumerate-active-directory-users
type: command
executor: bash
data: 'GetADUsers.py ''$_DOMAIN/$_USERNAME:$_PASSWORD'' -dc-ip $_DOMAIN_IP -all'
output: >-
  root@kali:~# GetADUsers.py 'host.domain/DomainUser:secretpassword' -dc-ip
  10.10.10.10 -all 

  Impacket v0.9.21-dev - Copyright 2019 SecureAuth Corporation


  [*] Querying 10.10.10.10 for information about domain.

  Name                  Email                           PasswordLastSet     
  LastLogon           

  --------------------  ------------------------------  ------------------- 
  -------------------

  Administrator                                         2018-07-18
  15:06:40.351723  2018-07-30 13:17:40.656520 

  Guest                                                 <never>             
  <never>             

  krbtgt                                                2018-07-18
  14:50:36.972031  <never>             

  DomainUser                                               2018-07-18
  16:14:38.402764  2018-07-21 10:01:30.320277
created_at: '2019-12-04T19:07:19.054377+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - discovery
verified: true
validated: true
---

# getadusers-enumerate-active-directory-users

## Command

```bash
GetADUsers.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -all
```

## Description

Enumerates all AD users with full details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| '$_DOMAIN/$_USERNAME:$_PASSWORD' | Credentials | Yes |
| -dc-ip $_DOMAIN_IP | DC IP | Yes |
| -all | Full details | Optional |

## Examples

### Enumerate

```bash
GetADUsers.py 'domain/user:pass' -dc-ip 10.10.10.10 -all
```

## Expected Output

User table.

## Related

- [[procedures/Enumerate-All-Active-Directory-Users]]
