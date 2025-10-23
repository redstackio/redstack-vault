---
id: c5b054c5-df55-45d9-9f90-ca103678c33a
name: "\tList .conf files in /etc (recursive 1 level)"
type: command
executor: bash
data: 'find /etc/ -maxdepth 1 -name *.conf -type f -exec ls -la {} \; 2>/dev/null

  ls -la /etc/*.conf

  '
output: null
created_at: '2020-07-14T18:14:41.288578+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# 	List .conf files in /etc (recursive 1 level)

```bash
find /etc/ -maxdepth 1 -name *.conf -type f -exec ls -la {} \; 2>/dev/null
ls -la /etc/*.conf

```


