---
id: 0ff7c2d8-e422-4c35-9e11-b37448f2f350
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:17.657134+00:00'
updated_at: '2023-04-10T20:34:12.040072+00:00'
---

# Code Snippet 0ff7c2d8

**Language**: Bash

```bash
# Removes the most recently logged command.
# Note that we actually have to delete two history entries at once,
# otherwise the `history -d` command itself will be logged as well.
history -d -2 && history -d -1
```


