---
id: 711e80b8-0aca-4c4b-8d0e-9369fbf57433
name: List of users with CONTROLAUTH
type: command
executor: bash
data: select distinct(grantee) from sysibm.systabauth where CONTROLAUTH='Y'
output: null
created_at: '2023-04-06T03:56:32.690094+00:00'
updated_at: '2023-04-10T20:22:02.658518+00:00'
---

# List of users with CONTROLAUTH

```bash
select distinct(grantee) from sysibm.systabauth where CONTROLAUTH='Y'
```


