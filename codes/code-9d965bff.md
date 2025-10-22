---
id: 9d965bff-e1d0-46e1-a218-4c410b9841f5
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:37.036699+00:00'
updated_at: '2023-04-10T20:24:31.988533+00:00'
---

# Code Snippet 9d965bff

**Language**: SQL

```sql
and (SELECT count(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' ) < number_of_table
```
