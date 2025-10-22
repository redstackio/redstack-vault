---
id: d4740836-06ca-418f-b0fd-5b57fc944861
name: Ignore specific commands from being saved in history
type: command
executor: bash
data: HISTIGNORE=$HISTIGNORE:"ls -l"
output: null
created_at: '2023-04-06T03:56:17.656832+00:00'
updated_at: '2023-04-10T20:34:12.038683+00:00'
---

# Ignore specific commands from being saved in history

```bash
HISTIGNORE=$HISTIGNORE:"ls -l"
```
