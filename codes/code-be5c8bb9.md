---
id: be5c8bb9-9887-46cc-a144-c6a2ed39921f
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:33.737937+00:00'
updated_at: '2023-04-10T20:22:43.469322+00:00'
---

# Code Snippet be5c8bb9

**Language**: SQL

```sql
MSSQL 2000:
SELECT name, password FROM master..sysxlogins
SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins (Need to convert to hex to return hashes in MSSQL error message / some version of query analyzer.)

MSSQL 2005
SELECT name, password_hash FROM master.sys.sql_logins
SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
```
