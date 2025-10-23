---
id: 18d13e43-87c7-444d-8ead-7cb1d220cc28
name: "\tFind .conf files (recursive 4 levels) and output line number where the word\
  \ ‘password’ is located"
type: command
executor: bash
data: 'find / -maxdepth 4 -name *.conf -type f -exec grep -Hn password {} \; 2>/dev/null

  '
output: null
created_at: '2020-07-14T18:14:41.288737+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# 	Find .conf files (recursive 4 levels) and output line number where the word ‘password’ is located

```bash
find / -maxdepth 4 -name *.conf -type f -exec grep -Hn password {} \; 2>/dev/null

```


