---
id: eba54f9c-d81e-42a8-b6b2-15bbca0703ef
name: Remove the SPN
type: command
executor: bash
data: PowerView2 > Set-DomainObject -Identity username -Clear serviceprincipalname
output: null
created_at: '2023-04-06T03:56:06.700908+00:00'
updated_at: '2023-04-10T20:26:07.517652+00:00'
---

# Remove the SPN

```bash
PowerView2 > Set-DomainObject -Identity username -Clear serviceprincipalname
```


