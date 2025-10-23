---
id: 266b69d1-bcc4-4325-898d-fc142bb17079
name: List needed shared libraries and RPATH of flag15
type: command
executor: bash
data: readelf -d flag15 | egrep "NEEDED|RPATH"
output: null
created_at: '2023-04-06T03:56:19.400857+00:00'
updated_at: '2023-04-10T20:34:31.017246+00:00'
---

# List needed shared libraries and RPATH of flag15

```bash
readelf -d flag15 | egrep "NEEDED|RPATH"
```


