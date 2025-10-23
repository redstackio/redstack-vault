---
id: db0b66f1-54bc-48a0-bc35-f56c44cb9471
name: Retrieve name and password hash from sql_logins table in MSSQL 2005
type: command
executor: bash
data: SELECT name, password_hash FROM master.sys.sql_logins
output: null
created_at: '2023-04-06T03:56:33.738217+00:00'
updated_at: '2023-04-10T20:22:43.467446+00:00'
---

# Retrieve name and password hash from sql_logins table in MSSQL 2005

```bash
SELECT name, password_hash FROM master.sys.sql_logins
```


