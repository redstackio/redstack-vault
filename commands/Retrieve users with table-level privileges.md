---
id: 2a2e05a9-6fc8-43d8-b0f1-f35e50c431ca
name: Retrieve users with table-level privileges
type: command
executor: bash
data: select distinct(grantee) from sysibm.systabauth
output: null
created_at: '2023-04-06T03:56:32.616080+00:00'
updated_at: '2023-04-10T20:22:05.508378+00:00'
---

# Retrieve users with table-level privileges

```bash
select distinct(grantee) from sysibm.systabauth
```
