---
id: aa04c2ca-dd40-4b11-8c16-8a1824ab2a75
name: Retrieve users with database-level privileges
type: command
executor: bash
data: select grantee from syscat.dbauth
output: null
created_at: '2023-04-06T03:56:32.616002+00:00'
updated_at: '2023-04-10T20:22:05.508378+00:00'
---

# Retrieve users with database-level privileges

```bash
select grantee from syscat.dbauth
```
