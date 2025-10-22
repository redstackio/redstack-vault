---
id: c2bc137f-c411-442c-b347-c2b99e4ce5f8
name: Start two listeners on Attacker machine
type: command
executor: bash
data: 'nc -lvp 8080

  nc -lvp 8081

  '
output: null
created_at: '2023-04-06T03:56:24.592489+00:00'
updated_at: '2023-04-10T20:25:31.686351+00:00'
---

# Start two listeners on Attacker machine

```bash
nc -lvp 8080
nc -lvp 8081

```
