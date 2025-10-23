---
id: 40a0efa9-c4d3-46af-8860-351ac3bd422e
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:33.953210+00:00'
updated_at: '2023-04-10T20:22:46.088423+00:00'
---

# Code Snippet 40a0efa9

**Language**: SQL

```sql
EXEC sp_configure 'show advanced options',1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell',1;
RECONFIGURE;
```


