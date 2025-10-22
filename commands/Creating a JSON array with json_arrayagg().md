---
id: ef197464-1d45-40e1-9c0c-c6a7c0fb3931
name: Creating a JSON array with json_arrayagg()
type: command
executor: bash
data: SELECT json_arrayagg(name) FROM users;
output: null
created_at: '2023-04-06T03:56:34.912781+00:00'
updated_at: '2023-04-10T20:22:50.539408+00:00'
---

# Creating a JSON array with json_arrayagg()

```bash
SELECT json_arrayagg(name) FROM users;
```
