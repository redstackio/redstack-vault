---
id: 50fa4f0b-8470-48ba-9c77-41f0e97d2ea2
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:19.522207+00:00'
updated_at: '2023-04-10T20:34:27.485390+00:00'
---

# Code Snippet 50fa4f0b

**Language**: Powershell

```powershell
# build a simple alpine image
git clone https://github.com/saghul/lxd-alpine-builder
./build-alpine -a i686

# import the image
lxc image import ./alpine.tar.gz --alias myimage

# run the image
lxc init myimage mycontainer -c security.privileged=true

# mount the /root into the image
lxc config device add mycontainer mydevice disk source=/ path=/mnt/root recursive=true

# interact with the container
lxc start mycontainer
lxc exec mycontainer /bin/sh
```
