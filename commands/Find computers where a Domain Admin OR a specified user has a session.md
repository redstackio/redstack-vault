---
id: ff9c4dce-fc93-4e30-8eba-fa9f596e791e
name: Find computers where a Domain Admin OR a specified user has a session
type: command
executor: bash
data: 'Invoke-UserHunter

  Invoke-UserHunter -GroupName "RDPUsers"

  Invoke-UserHunter -Stealth'
output: null
created_at: '2023-04-06T03:56:02.231218+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
---

# Find computers where a Domain Admin OR a specified user has a session

```bash
Invoke-UserHunter
Invoke-UserHunter -GroupName "RDPUsers"
Invoke-UserHunter -Stealth
```
