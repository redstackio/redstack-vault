---
id: ebbfd331-774e-489d-8e09-06204b30b441
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:34.943638+00:00'
updated_at: '2023-04-10T20:22:57.309257+00:00'
---

# Code Snippet ebbfd331

**Language**: SQL

```sql
SELECT json_arrayagg(concat_ws(0x3a,table_schema,table_name)) from INFORMATION_SCHEMA.TABLES;
```


