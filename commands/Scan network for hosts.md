---
id: 8b7de332-c7f5-4a8c-8055-e3a811b1dff6
name: Scan network for hosts
type: command
executor: bash
data: netdiscover -i eth0 -r 192.168.1.0/24
output: null
created_at: '2023-04-06T03:56:22.242964+00:00'
updated_at: '2023-04-10T20:25:08.368190+00:00'
---

# Scan network for hosts

```bash
netdiscover -i eth0 -r 192.168.1.0/24
```
