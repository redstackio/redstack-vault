---
id: b48d6f2b-72e6-46c7-ade3-f6317565e11b
name: MSSQL
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:00.953858+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# MSSQL

# SQLCMD

**Command** ([[List Databases]]):

```bash
sqlcmd -E -S localhost -Q "EXEC sp_databases;"

```

**Command** ([[List Tables in Database]]):

```bash
sqlcmd -E -S localhost -Q "SELECT * FROM DatabaseName.information_schema.tables;" -W -w 999 -s"," -o "c:\windows\temp\RecruiterProd_MSCRM_tables.csv"

```

**Command** ([[Retrieve table contents]]):

```bash
sqlcmd -E -S localhost -d DatabaseName -Q "SELECT * FROM SystemUserBase;" -W -w 999 -s"," -o "c:\windows\temp\RecruiterProd_MSCRM_userbase.csv"

```

**Command** ([[Dump MSSQL Password Hashes]]):

```bash
sqlcmd -E -S localhost -Q "SELECT name, password_hash FROM master.sys.sql_logins;"

```
