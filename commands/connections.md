---
id: 91c8fdf3-01f5-48a4-8629-1fdc6e5f4b5c
name: connections
type: command
executor: bash
data: 'lsof -i | awk ''{print $8}'' | sort | uniq -c | grep ''TCP\|UDP''

  '
output: null
created_at: '2020-07-14T18:21:25.727001+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# connections

```bash
lsof -i | awk '{print $8}' | sort | uniq -c | grep 'TCP\|UDP'

```
