---
id: fe4e300b-a443-4457-8219-092408ea2965
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:33.284527+00:00'
updated_at: '2023-04-10T20:22:26.625356+00:00'
---

# Code Snippet fe4e300b

**Language**: SQL

```sql
from BlogPosts
where title like '%'
  and DOESNT_EXIST=1 and ''='%' -- 
  and published = true
```
