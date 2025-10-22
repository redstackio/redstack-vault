---
id: 295ae896-1841-4bd4-9034-093d04f9aa64
name: Show privileges for current user on database
type: command
executor: bash
data: select * from syscat.dbauth where grantee = current user
output: null
created_at: '2023-04-06T03:56:32.653063+00:00'
updated_at: '2023-04-10T20:22:04.113006+00:00'
---

# Show privileges for current user on database

```bash
select * from syscat.dbauth where grantee = current user
```
