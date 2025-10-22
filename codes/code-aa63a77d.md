---
id: aa63a77d-dd0c-4152-b742-5a591ecab3f9
type: code
language: Bash
verified: false
created_at: '2020-03-23T01:27:24.694042+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet aa63a77d

**Language**: Bash

```bash
for FILE in $(find /var/log -name "auth.log" 2>/dev/null); do shred -z $FILE; cat /dev/null > $FILE; done
```
