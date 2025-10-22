---
id: 35c82b30-b285-41f8-9fe3-2276116f1525
name: established
type: command
executor: bash
data: 'lsof -i -nP | grep ESTABLISHED | awk ''{print $1, $9}'' | sort -u

  '
output: null
created_at: '2020-07-14T18:21:25.727207+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# established

```bash
lsof -i -nP | grep ESTABLISHED | awk '{print $1, $9}' | sort -u

```
