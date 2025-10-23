---
id: 33626441-8cbf-4789-8c82-4ee236e2fb19
name: Run Ubuntu container with privileged access
type: command
executor: bash
data: sudo docker -H unix:///google/host/var/run/docker.sock run -v /:/host -it ubuntu
  chroot /host /bin/bash
output: null
created_at: '2023-04-06T03:56:19.469298+00:00'
updated_at: '2023-04-10T20:34:34.755994+00:00'
---

# Run Ubuntu container with privileged access

```bash
sudo docker -H unix:///google/host/var/run/docker.sock run -v /:/host -it ubuntu chroot /host /bin/bash
```


