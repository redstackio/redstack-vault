---
id: 8b63bb63-640e-452f-a908-cb4e5cedfb33
name: Add cap_net_raw+p to ping binary
type: command
executor: bash
data: /usr/bin/setcap cap_net_raw+p /bin/ping
output: null
created_at: '2023-04-06T03:56:18.886416+00:00'
updated_at: '2023-04-10T20:34:33.054247+00:00'
---

# Add cap_net_raw+p to ping binary

```bash
/usr/bin/setcap cap_net_raw+p /bin/ping
```
