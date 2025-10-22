---
id: 139038ae-4e63-4c84-96fe-4d1b6eea1f82
name: Start the newly created container
type: command
executor: bash
data: curl -XPOST –unix-socket /var/run/docker.sock http://localhost/containers/ID_FROM_PREVIOUS_COMMAND/start
output: null
created_at: '2023-04-06T03:56:16.917105+00:00'
updated_at: '2023-04-10T20:33:49.704451+00:00'
---

# Start the newly created container

```bash
curl -XPOST –unix-socket /var/run/docker.sock http://localhost/containers/ID_FROM_PREVIOUS_COMMAND/start
```
