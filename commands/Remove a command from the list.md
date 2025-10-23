---
id: d4138cf0-b944-4cd3-b45c-f831fc39aef7
name: Remove a command from the list
type: command
executor: bash
data: HISTIGNORE=${HISTIGNORE%%:"ls -l"*}
output: null
created_at: '2023-04-06T03:56:17.656886+00:00'
updated_at: '2023-04-10T20:34:12.038683+00:00'
---

# Remove a command from the list

```bash
HISTIGNORE=${HISTIGNORE%%:"ls -l"*}
```


