---
id: 6aae448a-96b2-487f-9565-b63088004bb3
name: Start Netsh Capture with Persistence
type: command
executor: bash
data: netsh trace start capture=yes report=disabled persistent=yes tracefile=c:\trace.etl
  maxsize=16384
output: null
created_at: '2023-04-06T03:56:23.097114+00:00'
updated_at: '2023-04-10T20:25:12.038720+00:00'
---

# Start Netsh Capture with Persistence

```bash
netsh trace start capture=yes report=disabled persistent=yes tracefile=c:\trace.etl maxsize=16384
```
