---
id: c4981e8f-17e8-445d-98d2-a897e2c025ef
name: Retrieve database and instance service and build level
type: command
executor: bash
data: select service_level,bld_level from sysibmadm.env_inst_info
output: null
created_at: '2023-04-06T03:56:32.535901+00:00'
updated_at: '2023-04-10T20:21:57.272196+00:00'
---

# Retrieve database and instance service and build level

```bash
select service_level,bld_level from sysibmadm.env_inst_info
```
