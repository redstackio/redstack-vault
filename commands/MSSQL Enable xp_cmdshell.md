---
id: 762370fe-9698-49f7-9385-dde64daf52bb
name: MSSQL Enable xp_cmdshell
type: command
executor: default
data: 'EXEC sp_configure ''show advanced options'', 1

  go

  RECONFIGURE

  go

  EXEC sp_configure ''xp_cmdshell'', 1

  go

  RECONFIGURE

  go'
output: '1> EXEC sp_configure ''show advanced options'', 1

  2> go

  Configuration option ''show advanced options'' changed from 1 to 1. Run the RECONFIGURE
  statement to install.

  (return status = 0)

  1> RECONFIGURE

  2> go

  1> EXEC sp_configure ''xp_cmdshell'', 1

  2> go

  Configuration option ''xp_cmdshell'' changed from 1 to 1. Run the RECONFIGURE statement
  to install.

  (return status = 0)

  1> RECONFIGURE

  2> go'
created_at: '2020-07-07T00:44:44.630688+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# MSSQL Enable xp_cmdshell

```default
EXEC sp_configure 'show advanced options', 1
go
RECONFIGURE
go
EXEC sp_configure 'xp_cmdshell', 1
go
RECONFIGURE
go
```

## Expected Output

```
1> EXEC sp_configure 'show advanced options', 1
2> go
Configuration option 'show advanced options' changed from 1 to 1. Run the RECONFIGURE statement to install.
(return status = 0)
1> RECONFIGURE
2> go
1> EXEC sp_configure 'xp_cmdshell', 1
2> go
Configuration option 'xp_cmdshell' changed from 1 to 1. Run the RECONFIGURE statement to install.
(return status = 0)
1> RECONFIGURE
2> go
```


