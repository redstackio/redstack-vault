---
id: 21714dda-23a8-489a-a342-f08eef22b9da
name: List Databases
type: command
executor: bash
data: 'sqlcmd -E -S localhost -Q "EXEC sp_databases;"

  '
output: null
created_at: '2020-07-14T18:21:00.905928+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List Databases

```bash
sqlcmd -E -S localhost -Q "EXEC sp_databases;"

```


