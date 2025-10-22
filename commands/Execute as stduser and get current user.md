---
id: d9dc2174-a84f-4e76-b1d5-9eb6f70bb1cb
name: Execute as stduser and get current user
type: command
executor: bash
data: 'EXECUTE AS LOGIN = ''stduser''

  SELECT SYSTEM_USER'
output: null
created_at: '2023-04-06T03:56:21.083460+00:00'
updated_at: '2023-04-10T20:36:46.097015+00:00'
---

# Execute as stduser and get current user

```bash
EXECUTE AS LOGIN = 'stduser'
SELECT SYSTEM_USER
```
