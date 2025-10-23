---
id: c9a31a82-e32a-4b1f-8f63-972a2ed50566
type: code
language: Oracle SQL
verified: false
created_at: '2023-04-06T03:56:33.371121+00:00'
updated_at: '2023-04-10T20:22:26.996569+00:00'
---

# Code Snippet c9a31a82

**Language**: Oracle SQL

```oracle sql
NVL(TO_CHAR(DBMS_XMLGEN.getxml('select 1 where 1337>1')),'1')!='1'
```


