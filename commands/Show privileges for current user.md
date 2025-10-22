---
id: 738899f5-4cc5-40d5-aba0-018acf7911fc
name: Show privileges for current user
type: command
executor: bash
data: select * from syscat.tabauth where grantee = current user
output: null
created_at: '2023-04-06T03:56:32.653023+00:00'
updated_at: '2023-04-10T20:22:04.113006+00:00'
---

# Show privileges for current user

```bash
select * from syscat.tabauth where grantee = current user
```
