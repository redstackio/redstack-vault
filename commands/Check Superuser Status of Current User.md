---
id: 95d8598b-fa51-4665-bf7a-5303991155bd
name: Check Superuser Status of Current User
type: command
executor: bash
data: SELECT usesuper FROM pg_user WHERE usename = CURRENT_USER;
output: null
created_at: '2023-04-06T03:56:35.596511+00:00'
updated_at: '2023-04-10T20:23:22.132689+00:00'
---

# Check Superuser Status of Current User

```bash
SELECT usesuper FROM pg_user WHERE usename = CURRENT_USER;
```


