---
id: 06b83c07-8e50-41cf-8bd7-4980d4866bb5
name: Remove cap_net_raw from ping binary
type: command
executor: bash
data: /usr/bin/setcap -r /bin/ping
output: null
created_at: '2023-04-06T03:56:18.886484+00:00'
updated_at: '2023-04-10T20:34:33.054247+00:00'
---

# Remove cap_net_raw from ping binary

```bash
/usr/bin/setcap -r /bin/ping
```
