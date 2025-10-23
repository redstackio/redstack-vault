---
id: ddf208d0-d8d9-49d8-9a88-3d59d21b19e7
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:35.879614+00:00'
updated_at: '2023-04-10T20:23:16.533492+00:00'
---

# Code Snippet ddf208d0

**Language**: SQL

```sql
select case when substring(table_name,1,1)='a' then pg_sleep(5) else pg_sleep(0) end from information_schema.tables limit 1
```


