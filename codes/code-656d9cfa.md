---
id: 656d9cfa-5b9f-41c5-b900-5f79fc2f466f
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:20.266620+00:00'
updated_at: '2023-04-10T20:36:43.583969+00:00'
---

# Code Snippet 656d9cfa

**Language**: SQL

```sql
EXEC sp_configure 'show advanced options',1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell',1;
RECONFIGURE;
```
