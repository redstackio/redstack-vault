---
id: 3b40a6e6-3175-454b-b399-0aface1bd400
name: Open a shell in a container
type: command
executor: bash
data: sk exec -it <pod-name> -c <container-name> -- /bin/sh
output: null
created_at: '2023-04-06T03:55:51.871666+00:00'
updated_at: '2023-04-10T20:21:11.927463+00:00'
---

# Open a shell in a container

```bash
sk exec -it <pod-name> -c <container-name> -- /bin/sh
```
