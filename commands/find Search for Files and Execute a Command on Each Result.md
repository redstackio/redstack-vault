---
id: 3d93bcf2-ac37-41ee-b477-371633c8dbd0
name: find Search for Files and Execute a Command on Each Result
type: command
executor: ''
data: find $_DIRECTORY -exec $_CMD $_ARG1 $_ARG2 {} \; 2>/dev/null
output: null
created_at: '2019-09-17T06:24:10.218539+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# find Search for Files and Execute a Command on Each Result

```bash
find $_DIRECTORY -exec $_CMD $_ARG1 $_ARG2 {} \; 2>/dev/null
```
