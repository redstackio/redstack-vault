---
id: e55f35d6-0337-4499-bae7-207e8343aefd
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:17.808936+00:00'
updated_at: '2023-04-10T20:34:10.432569+00:00'
---

# Code Snippet e55f35d6

**Language**: Bash

```bash
ORIG_TIME=$(date)
date -s "2022-10-31 23:59:59"
touch -a -m "example"
date -s "${ORIG_TIME}"
```


