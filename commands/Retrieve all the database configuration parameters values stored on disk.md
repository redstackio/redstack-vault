---
id: b2add254-46b3-48ce-8414-b2141c140c85
name: Retrieve all the database configuration parameters values stored on disk
type: command
executor: bash
data: select name, deferred_value, dbpartitionnum from sysibmadm.dbcfg -- Requires
  priv.
output: null
created_at: '2023-04-06T03:56:33.205039+00:00'
updated_at: '2023-04-10T20:22:01.198376+00:00'
---

# Retrieve all the database configuration parameters values stored on disk

```bash
select name, deferred_value, dbpartitionnum from sysibmadm.dbcfg -- Requires priv.
```


