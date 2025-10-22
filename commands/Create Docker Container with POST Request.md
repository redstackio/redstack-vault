---
id: 3c8f150c-03ae-43b4-b8f9-75bcab794494
name: Create Docker Container with POST Request
type: command
executor: bash
data: '$ curl –insecure -X POST -H "Content-Type: application/json" https://tls-opendocker.socket2376/containers/create?name=test
  -d ''{"Image":"alpine", "Cmd":["/usr/bin/tail", "-f", "1234", "/dev/null"], "Binds":
  [ "/:/mnt" ], "Privileged": true}'''
output: null
created_at: '2023-04-06T03:56:16.968832+00:00'
updated_at: '2023-04-10T20:33:46.886185+00:00'
---

# Create Docker Container with POST Request

```bash
$ curl –insecure -X POST -H "Content-Type: application/json" https://tls-opendocker.socket2376/containers/create?name=test -d '{"Image":"alpine", "Cmd":["/usr/bin/tail", "-f", "1234", "/dev/null"], "Binds": [ "/:/mnt" ], "Privileged": true}'
```
