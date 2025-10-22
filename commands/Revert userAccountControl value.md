---
id: c99b5c97-e083-4ac9-ba4a-ef153cdb9fc6
name: Revert userAccountControl value
type: command
executor: bash
data: PowerView2 > Set-DomainObject -Identity username -XOR @{useraccountcontrol=4194304}
  -Verbose
output: null
created_at: '2023-04-06T03:56:06.701206+00:00'
updated_at: '2023-04-10T20:26:07.517652+00:00'
---

# Revert userAccountControl value

```bash
PowerView2 > Set-DomainObject -Identity username -XOR @{useraccountcontrol=4194304} -Verbose
```
