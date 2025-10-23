---
id: 1cb95e39-f9ed-427e-834a-b133d8364b39
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:37.001678+00:00'
updated_at: '2023-04-10T20:24:32.669428+00:00'
---

# Code Snippet 1cb95e39

**Language**: SQL

```sql
SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'
```


