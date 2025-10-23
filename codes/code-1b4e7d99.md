---
id: 1b4e7d99-906c-4163-af6a-0d09bb4ebbba
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:37.093285+00:00'
updated_at: '2023-04-10T20:24:28.480455+00:00'
---

# Code Snippet 1b4e7d99

**Language**: SQL

```sql
CASE WHEN (SELECT hex(substr(sql,1,1)) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset 0) = hex('some_char') THEN <order_element_1> ELSE <order_element_2> END
```


