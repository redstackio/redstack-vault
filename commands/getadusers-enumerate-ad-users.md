---
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
platforms:
  - Linux
  - Windows
tags:
  - ad
  - enum
verified: true
validated: true
---

# getadusers-enumerate-ad-users

## Command

```bash
GetADUsers.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -all
```

## Description

This command uses the Impacket GetADUsers.py tool to enumerate all Active Directory users in a domain, retrieving detailed attributes such as names, emails, last logon times, and password last set dates. It requires valid domain credentials and connects to a specified domain controller via LDAP. Use this during authenticated reconnaissance to map user accounts for targeting in further attacks like lateral movement or privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| '$_DOMAIN/$_USERNAME:$_PASSWORD' | Domain credentials in the format 'domain/username:password' for LDAP authentication | Yes |
| -dc-ip $_DOMAIN_IP | IP address of the domain controller to query | Yes |
| -all | Flag to retrieve all available user attributes (e.g., email, logon info); without it, only basic info is shown | No |

## Examples

### Basic Usage

```bash
GetADUsers.py 'example.com/user:pass' -dc-ip 10.10.10.10 -all
```

This runs the enumeration with full details on a domain controller at 10.10.10.10.

### Advanced Usage

```bash
GetADUsers.py 'example.com/user:pass' -dc-ip 10.10.10.10 -all --dc-port 636
```

This uses LDAPS (secure LDAP) on port 636 for encrypted communication.

## Expected Output

The command outputs a table of enumerated users with their attributes. Successful execution looks like:

```
root@kali:~# GetADUsers.py 'host.domain/DomainUser:secretpassword' -dc-ip 10.10.10.10 -all 
Impacket v0.9.21-dev - Copyright 2019 SecureAuth Corporation

[*] Querying 10.10.10.10 for information about domain.
Name                  Email                           PasswordLastSet      LastLogon           
--------------------  ------------------------------  -------------------  -------------------
Administrator                                         2018-07-18 15:06:40.351723  2018-07-30 13:17:40.656520 
Guest                                                 <never>              <never>             
krbtgt                                                2018-07-18 14:50:36.972031  <never>             
DomainUser                                               2018-07-18 16:14:38.402764  2018-07-21 10:01:30.320277
```

Look for the table listing users without errors like authentication failures.

## Related

- [[procedures/enumerate-active-directory-users-authenticated]]
- [[tools/impacket-getadusers]] (Parent tool documentation)
