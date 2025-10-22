---
id: fbd53fd2-70ed-480f-9b04-6bd959ded9ed
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:17.743017+00:00'
updated_at: '2023-04-10T20:34:10.816328+00:00'
---

# Code Snippet fbd53fd2

**Language**: Bash

```bash
echo "sneaky-payload-command" > script.sh
echo "# $(clear)" >> script.sh
echo "# Do not remove. Generated from /etc/issue.conf by configure." >> script.sh

# When printed, the terminal will be cleared and only the last line will be visible:
cat script.sh
```
