---
id: 0e1c2b4e-1991-4c20-926b-dd2feceb8078
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:33.284597+00:00'
updated_at: '2023-04-10T20:22:26.625356+00:00'
---

# Code Snippet 0e1c2b4e

**Language**: SQL

```sql
org.hibernate.exception.SQLGrammarException: Column "DOESNT_EXIST" not found; SQL statement:
      select blogposts0_.id as id21_, blogposts0_.author as author21_, blogposts0_.promoCode as promo3_21_, blogposts0_.title as title21_, blogposts0_.published as published21_ from BlogPosts blogposts0_ where blogposts0_.title like '%' or DOESNT_EXIST='%' and blogposts0_.published=1 [42122-159]
```
