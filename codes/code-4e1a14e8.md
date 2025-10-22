---
id: 4e1a14e8-8bd6-4573-a11a-60cd69922b0a
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:33.305044+00:00'
updated_at: '2023-04-10T20:22:26.250391+00:00'
---

# Code Snippet 4e1a14e8

**Language**: SQL

```sql
from BlogPosts
where title like '%11'
  and (select password from User where username='admin')=1
  or ''='%'
  and published = true
```
