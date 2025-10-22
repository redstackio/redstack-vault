---
id: 6ed79a12-5c79-4caa-b259-8914ff6f6bdd
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:37.018191+00:00'
updated_at: '2023-04-10T20:24:31.294791+00:00'
---

# Code Snippet 6ed79a12

**Language**: SQL

```sql
SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='table_name' LIMIT X+1 OFFSET X
```
