---
id: cb5c403a-56f0-45e7-9c4c-f5563afdc14e
name: Check Current User Superuser Privileges
type: command
executor: bash
data: SELECT current_setting('is_superuser');
output: null
created_at: '2023-04-06T03:56:35.596487+00:00'
updated_at: '2023-04-10T20:23:22.132689+00:00'
---

# Check Current User Superuser Privileges

```bash
SELECT current_setting('is_superuser');
```


