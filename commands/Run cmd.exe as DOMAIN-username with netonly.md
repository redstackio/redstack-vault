---
id: 542b3302-bc69-4ae1-bb5e-d817789815d4
name: Run cmd.exe as DOMAIN\username with netonly
type: command
executor: bash
data: runas /netonly /user:DOMAIN\username "cmd.exe"
output: null
created_at: '2023-04-06T03:56:31.371580+00:00'
updated_at: '2023-04-10T20:38:03.484250+00:00'
---

# Run cmd.exe as DOMAIN\username with netonly

```bash
runas /netonly /user:DOMAIN\username "cmd.exe"
```
