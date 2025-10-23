---
id: 3421101e-9bad-4592-ba5b-983ce6c69f51
name: Check if user is a member of sysadmin role
type: command
executor: bash
data: SELECT is_srvrolemember('sysadmin')
output: null
created_at: '2023-04-06T03:56:20.649944+00:00'
updated_at: '2023-04-10T20:36:41.379800+00:00'
---

# Check if user is a member of sysadmin role

```bash
SELECT is_srvrolemember('sysadmin')
```


