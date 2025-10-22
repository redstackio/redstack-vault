---
id: dfebc175-8df1-4702-9812-0fb979d63079
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:21.128259+00:00'
updated_at: '2023-04-10T20:36:43.928288+00:00'
---

# Code Snippet dfebc175

**Language**: SQL

```sql
MSSQL 2000:
SELECT name, password FROM master..sysxlogins
SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins (Need to convert to hex to return hashes in MSSQL error message / some version of query analyzer.)

MSSQL 2005
SELECT name, password_hash FROM master.sys.sql_logins
SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
```
