---
id: ca25311f-3ac4-46ee-8e01-c4d85c79d905
name: "\tList files in specified directory (/var/log)"
type: command
executor: bash
data: 'find /var/log -type f -exec ls -la {} \; 2>/dev/null

  '
output: null
created_at: '2020-07-14T18:14:41.288040+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# 	List files in specified directory (/var/log)

```bash
find /var/log -type f -exec ls -la {} \; 2>/dev/null

```


