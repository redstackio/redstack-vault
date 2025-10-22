---
id: 72362784-7671-4bbb-af10-2110156ae6fd
name: Reverse SSH tunneling to local machine
type: command
executor: bash
data: ssh -R [bindaddr]:[port]:[localhost]:[localport] [user]@[host]
output: null
created_at: '2023-04-06T03:56:22.486127+00:00'
updated_at: '2023-04-10T20:25:19.128197+00:00'
---

# Reverse SSH tunneling to local machine

```bash
ssh -R [bindaddr]:[port]:[localhost]:[localport] [user]@[host]
```
