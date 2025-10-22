---
id: d95e6444-cb54-4581-acdf-57701faacae3
name: Run Debian container with access to host namespaces
type: command
executor: bash
data: sudo docker -H unix:///google/host/var/run/docker.sock run -it --privileged
  --pid=host debian nsenter -t 1 -m -u -n -i sh
output: null
created_at: '2023-04-06T03:56:19.469365+00:00'
updated_at: '2023-04-10T20:34:34.755994+00:00'
---

# Run Debian container with access to host namespaces

```bash
sudo docker -H unix:///google/host/var/run/docker.sock run -it --privileged --pid=host debian nsenter -t 1 -m -u -n -i sh
```
