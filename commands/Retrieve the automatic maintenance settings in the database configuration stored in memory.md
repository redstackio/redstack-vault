---
id: 721f2334-9bc9-426d-b48b-b6c2b1b1ce64
name: Retrieve the automatic maintenance settings in the database configuration stored
  in memory
type: command
executor: bash
data: select dbpartitionnum, name, value from sysibmadm.dbcfg where name like 'auto_%'
  -- Requires priv.
output: null
created_at: '2023-04-06T03:56:33.204927+00:00'
updated_at: '2023-04-10T20:22:01.198376+00:00'
---

# Retrieve the automatic maintenance settings in the database configuration stored in memory

```bash
select dbpartitionnum, name, value from sysibmadm.dbcfg where name like 'auto_%' -- Requires priv.
```
