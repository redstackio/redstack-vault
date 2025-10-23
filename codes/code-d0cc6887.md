---
id: d0cc6887-ec49-449e-af9e-6ffd5e9a0906
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:20.266570+00:00'
updated_at: '2023-04-10T20:36:43.583969+00:00'
---

# Code Snippet d0cc6887

**Language**: SQL

```sql
EXEC xp_cmdshell "net user";
EXEC master..xp_cmdshell 'whoami'
EXEC master.dbo.xp_cmdshell 'cmd.exe dir c:';
EXEC master.dbo.xp_cmdshell 'ping 127.0.0.1';
```


