---
id: 3144595e-1d68-49f7-b353-0acb0062bf94
name: Find lsass's pid
type: command
executor: bash
data: tasklist /fi "imagename eq lsass.exe"
output: null
created_at: '2023-04-06T03:56:27.177120+00:00'
updated_at: '2023-04-10T20:37:14.787792+00:00'
---

# Find lsass's pid

```bash
tasklist /fi "imagename eq lsass.exe"
```


