---
id: 65c2a704-d6d9-4c6c-bee9-5efa0f32faa8
name: Get SQL Tables from a Database
type: command
executor: bash
data: Get-SQLInstanceDomain | Get-SQLTable -DatabaseName <DBNameFromGet-SQLDatabaseCommand>
  -NoDefaults
output: null
created_at: '2023-04-06T03:56:19.912246+00:00'
updated_at: '2023-04-10T20:36:30.038895+00:00'
---

# Get SQL Tables from a Database

```bash
Get-SQLInstanceDomain | Get-SQLTable -DatabaseName <DBNameFromGet-SQLDatabaseCommand> -NoDefaults
```


