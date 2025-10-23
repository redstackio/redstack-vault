---
id: 815f93cb-2dcc-4f77-9157-c9ab597abd04
name: Create a new container
type: command
executor: bash
data: 'curl -XPOST –unix-socket /var/run/docker.sock -d ''{"Image":"nginx"}'' -H ''Content-Type:
  application/json'' http://localhost/containers/create'
output: null
created_at: '2023-04-06T03:56:16.917057+00:00'
updated_at: '2023-04-10T20:33:49.704451+00:00'
---

# Create a new container

```bash
curl -XPOST –unix-socket /var/run/docker.sock -d '{"Image":"nginx"}' -H 'Content-Type: application/json' http://localhost/containers/create
```


