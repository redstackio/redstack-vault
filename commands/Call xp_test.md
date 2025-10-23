---
id: 90ad1b2f-c4ea-414a-8b93-a264385c8246
name: Call xp_test
type: command
executor: bash
data: Get-SQLQuery -UserName sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>"
  -Query "EXEC xp_test"
output: null
created_at: '2023-04-06T03:56:20.295483+00:00'
updated_at: '2023-04-10T20:36:30.722000+00:00'
---

# Call xp_test

```bash
Get-SQLQuery -UserName sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Query "EXEC xp_test"
```


