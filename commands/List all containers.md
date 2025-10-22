---
id: 3288ba81-f8c7-4ffb-8962-75fa8b8828c4
name: List all containers
type: command
executor: bash
data: curl --unix-socket /var/run/docker.sock http://127.0.0.1/containers/json
output: null
created_at: '2023-04-06T03:56:16.917000+00:00'
updated_at: '2023-04-10T20:33:49.704451+00:00'
---

# List all containers

```bash
curl --unix-socket /var/run/docker.sock http://127.0.0.1/containers/json
```
