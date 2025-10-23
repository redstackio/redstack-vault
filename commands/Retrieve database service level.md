---
id: a02dbc20-06b1-436f-a82d-b2f3e04f3624
name: Retrieve database service level
type: command
executor: bash
data: select service_level from table(sysproc.env_get_inst_info()) as instanceinfo
output: null
created_at: '2023-04-06T03:56:32.535738+00:00'
updated_at: '2023-04-10T20:21:57.272196+00:00'
---

# Retrieve database service level

```bash
select service_level from table(sysproc.env_get_inst_info()) as instanceinfo
```


