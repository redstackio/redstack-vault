---
id: a516c932-869c-42c4-b71c-ad6f13c3d42a
name: Reverse SSH tunneling to remote machine
type: command
executor: bash
data: ssh -R 3389:10.1.1.224:3389 root@10.11.0.32
output: null
created_at: '2023-04-06T03:56:22.486186+00:00'
updated_at: '2023-04-10T20:25:19.128197+00:00'
---

# Reverse SSH tunneling to remote machine

```bash
ssh -R 3389:10.1.1.224:3389 root@10.11.0.32
```


