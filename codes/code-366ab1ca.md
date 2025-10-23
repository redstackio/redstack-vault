---
id: 366ab1ca-3248-48c7-9775-578582ef580c
type: code
language: Bash
verified: false
created_at: '2019-10-31T21:16:30.125010+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 366ab1ca

**Language**: Bash

```bash
for FILE in $(find /var/log -name "auth.log" 2>/dev/null); do shred -z $FILE; cat /dev/null > $FILE; done
```


