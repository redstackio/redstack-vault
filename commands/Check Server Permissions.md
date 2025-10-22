---
id: cdd8f416-d08c-49c3-85f3-bf3474c5607f
name: Check Server Permissions
type: command
executor: bash
data: SELECT * FROM fn_my_permissions(NULL, 'SERVER');
output: null
created_at: '2023-04-06T03:56:34.157655+00:00'
updated_at: '2023-04-10T20:22:47.331484+00:00'
---

# Check Server Permissions

```bash
SELECT * FROM fn_my_permissions(NULL, 'SERVER');
```
