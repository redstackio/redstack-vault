---
id: 4e8f872d-31ed-4256-b80e-47cc0b594e8c
name: Start Netsh Capture with Filters
type: command
executor: bash
data: netsh trace start capture=yes report=disabled Ethernet.Type=IPv4 IPv4.Address=10.200.200.3
  tracefile=c:\trace.etl maxsize=16384
output: null
created_at: '2023-04-06T03:56:23.097239+00:00'
updated_at: '2023-04-10T20:25:12.038720+00:00'
---

# Start Netsh Capture with Filters

```bash
netsh trace start capture=yes report=disabled Ethernet.Type=IPv4 IPv4.Address=10.200.200.3 tracefile=c:\trace.etl maxsize=16384
```


