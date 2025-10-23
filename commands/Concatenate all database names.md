---
id: 66b9eaea-f398-4d35-a550-23d6945bd89d
name: Concatenate all database names
type: command
executor: bash
data: SELECT STRING_AGG(name, ', ') FROM master..sysdatabases; -- Change delimiter
  value such as ', ' to anything else you want => master, tempdb, model, msdb   (Only
  works in MSSQL 2017+)
output: null
created_at: '2023-04-06T03:56:33.639387+00:00'
updated_at: '2023-04-10T20:22:46.899409+00:00'
---

# Concatenate all database names

```bash
SELECT STRING_AGG(name, ', ') FROM master..sysdatabases; -- Change delimiter value such as ', ' to anything else you want => master, tempdb, model, msdb   (Only works in MSSQL 2017+)
```


