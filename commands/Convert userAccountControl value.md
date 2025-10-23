---
id: 74732c2e-3c70-400d-8860-f476d35f0300
name: Convert userAccountControl value
type: command
executor: bash
data: PowerView2 > Get-DomainUser username | ConvertFrom-UACValue
output: null
created_at: '2023-04-06T03:56:06.701254+00:00'
updated_at: '2023-04-10T20:26:07.517652+00:00'
---

# Convert userAccountControl value

```bash
PowerView2 > Get-DomainUser username | ConvertFrom-UACValue
```


