---
id: c8ae3809-aa50-4140-8c0b-b1ec9c9b7f2c
name: Run cmd.exe as DOMAIN\username with netonly and no profile
type: command
executor: bash
data: runas /noprofil /netonly /user:DOMAIN\username cmd.exe
output: null
created_at: '2023-04-06T03:56:31.371632+00:00'
updated_at: '2023-04-10T20:38:03.484250+00:00'
---

# Run cmd.exe as DOMAIN\username with netonly and no profile

```bash
runas /noprofil /netonly /user:DOMAIN\username cmd.exe
```
