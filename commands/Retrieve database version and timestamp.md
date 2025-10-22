---
id: 341790fd-9034-4aeb-a700-62ebd6c554d4
name: Retrieve database version and timestamp
type: command
executor: bash
data: select versionnumber, version_timestamp from sysibm.sysversions;
output: null
created_at: '2023-04-06T03:56:32.535683+00:00'
updated_at: '2023-04-10T20:21:57.272196+00:00'
---

# Retrieve database version and timestamp

```bash
select versionnumber, version_timestamp from sysibm.sysversions;
```
