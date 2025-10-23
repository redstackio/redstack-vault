---
id: 9dbbeb36-4af5-47a1-b6a5-dfe90023a6ef
name: 'View established connections of current machine:'
type: command
executor: bash
data: 'netstat -a -n -p tcp | find "ESTAB"

  '
output: null
created_at: '2020-07-14T18:21:27.746422+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# View established connections of current machine:

```bash
netstat -a -n -p tcp | find "ESTAB"

```


