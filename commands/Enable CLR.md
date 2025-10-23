---
id: bab533d7-e3e1-425b-adbd-993d2b1a40af
name: Enable CLR
type: command
executor: bash
data: 'sp_configure ''clr enabled'',1

  RECONFIGURE

  GO'
output: null
created_at: '2023-04-06T03:56:20.431310+00:00'
updated_at: '2023-04-10T20:36:42.151890+00:00'
---

# Enable CLR

```bash
sp_configure 'clr enabled',1
RECONFIGURE
GO
```


