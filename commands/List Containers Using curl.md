---
id: bd2b82a4-c341-4bb2-b02a-91a67cdb1457
name: List Containers Using curl
type: command
executor: bash
data: curl --unix-socket /var/run/docker.sock http://foo/containers/json
output: null
created_at: '2023-04-06T03:56:38.757122+00:00'
updated_at: '2023-04-10T20:24:05.013008+00:00'
---

# List Containers Using curl

```bash
curl --unix-socket /var/run/docker.sock http://foo/containers/json
```
