---
id: d0cc291d-6d43-476a-8146-b2f6c3f2435a
name: Check if current user has already an SPN setted
type: command
executor: bash
data: PowerView2 > Get-DomainUser -Identity <UserName> | select serviceprincipalname
output: null
created_at: '2023-04-06T03:56:06.700729+00:00'
updated_at: '2023-04-10T20:26:07.517652+00:00'
---

# Check if current user has already an SPN setted

```bash
PowerView2 > Get-DomainUser -Identity <UserName> | select serviceprincipalname
```
