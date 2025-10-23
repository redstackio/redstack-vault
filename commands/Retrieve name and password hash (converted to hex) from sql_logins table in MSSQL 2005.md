---
id: ff81f023-a0af-4f69-b4c6-b1dd82c69b05
name: Retrieve name and password hash (converted to hex) from sql_logins table in
  MSSQL 2005
type: command
executor: bash
data: SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
output: null
created_at: '2023-04-06T03:56:33.738244+00:00'
updated_at: '2023-04-10T20:22:43.467446+00:00'
---

# Retrieve name and password hash (converted to hex) from sql_logins table in MSSQL 2005

```bash
SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
```


