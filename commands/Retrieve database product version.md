---
id: d76b9034-c728-4c98-bb90-7ee6112bae94
name: Retrieve database product version
type: command
executor: bash
data: select getvariable('sysibm.version') from sysibm.sysdummy1 -- (v8+)
output: null
created_at: '2023-04-06T03:56:32.535787+00:00'
updated_at: '2023-04-10T20:21:57.272196+00:00'
---

# Retrieve database product version

```bash
select getvariable('sysibm.version') from sysibm.sysdummy1 -- (v8+)
```
