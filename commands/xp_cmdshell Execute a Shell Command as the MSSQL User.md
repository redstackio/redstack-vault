---
id: 8d235b78-bf94-4b57-8ec7-f43c76122c12
name: xp_cmdshell Execute a Shell Command as the MSSQL User
type: command
executor: default
data: 'EXEC xp_cmdshell "$_CMD"

  go'
output: '1> EXEC xp_cmdshell "whoami"

  2> go

  output

  ------------------------------------------------------------------

  ------------------------------------------------------------------

  ------------------------------------------------------------------

  nt service\mssql$sqlexpress

  NULL

  (2 rows affected, return status = 0)'
created_at: '2020-07-07T00:44:44.630930+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# xp_cmdshell Execute a Shell Command as the MSSQL User

```default
EXEC xp_cmdshell "$_CMD"
go
```

## Expected Output

```
1> EXEC xp_cmdshell "whoami"
2> go

output
------------------------------------------------------------------
------------------------------------------------------------------
------------------------------------------------------------------

nt service\mssql$sqlexpress
NULL
(2 rows affected, return status = 0)
```
