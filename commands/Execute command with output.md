---
id: 6526c9fa-81ff-4218-9966-062a42737ef9
name: Execute command with output
type: command
executor: bash
data: dcomexec.py -share C$ -object MMC20 '<DOMAIN>/<USERNAME>:<PASSWORD>@<MACHINE_CIBLE>'
  'ipconfig'
output: null
created_at: '2023-04-06T03:56:07.043136+00:00'
updated_at: '2023-04-10T20:26:18.160002+00:00'
---

# Execute command with output

```bash
dcomexec.py -share C$ -object MMC20 '<DOMAIN>/<USERNAME>:<PASSWORD>@<MACHINE_CIBLE>' 'ipconfig'
```
