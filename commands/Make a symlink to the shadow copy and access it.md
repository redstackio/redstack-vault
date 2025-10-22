---
id: c2c2a0b4-1a3a-4ea7-858f-3af95b2a1e32
name: Make a symlink to the shadow copy and access it
type: command
executor: bash
data: mklink /d c:\shadowcopy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\
output: null
created_at: '2023-04-06T03:56:30.010793+00:00'
updated_at: '2023-04-10T20:37:37.824369+00:00'
---

# Make a symlink to the shadow copy and access it

```bash
mklink /d c:\shadowcopy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\
```
