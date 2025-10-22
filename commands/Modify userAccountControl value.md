---
id: 2886295a-61de-4964-bfb2-bb16d976b58a
name: Modify userAccountControl value
type: command
executor: bash
data: PowerView2 > Set-DomainObject -Identity username -XOR @{useraccountcontrol=4194304}
  -Verbose
output: null
created_at: '2023-04-06T03:56:06.701077+00:00'
updated_at: '2023-04-10T20:26:07.517652+00:00'
---

# Modify userAccountControl value

```bash
PowerView2 > Set-DomainObject -Identity username -XOR @{useraccountcontrol=4194304} -Verbose
```
