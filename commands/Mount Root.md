---
id: 89e60607-7a69-4ca5-83aa-4a2be6d7c325
name: Mount Root
type: command
executor: bash
data: lxc config device add mycontainer mydevice disk source=/ path=/mnt/root recursive=true
output: null
created_at: '2023-04-06T03:56:19.522431+00:00'
updated_at: '2023-04-10T20:34:27.482023+00:00'
---

# Mount Root

```bash
lxc config device add mycontainer mydevice disk source=/ path=/mnt/root recursive=true
```
