---
id: 3c101383-366c-4771-a299-d56ec2c7b922
name: Check database permissions
type: command
executor: bash
data: SELECT * FROM fn_my_permissions (NULL, 'DATABASE');
output: null
created_at: '2023-04-06T03:56:34.157829+00:00'
updated_at: '2023-04-10T20:22:47.331484+00:00'
---

# Check database permissions

```bash
SELECT * FROM fn_my_permissions (NULL, 'DATABASE');
```


