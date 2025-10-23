---
id: 28835c28-e4d2-4fbc-89b7-c2a8a07e1d58
name: Check if user is sysadmin
type: command
executor: bash
data: SELECT IS_SRVROLEMEMBER('sysadmin')
output: null
created_at: '2023-04-06T03:56:21.083381+00:00'
updated_at: '2023-04-10T20:36:46.097015+00:00'
---

# Check if user is sysadmin

```bash
SELECT IS_SRVROLEMEMBER('sysadmin')
```


