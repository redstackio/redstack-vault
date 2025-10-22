---
id: 0c9e808f-2ae3-4c7e-81b9-56b107ba4eca
name: List all superusers
type: command
executor: bash
data: SELECT usename FROM pg_user WHERE usesuper IS TRUE
output: null
created_at: '2023-04-06T03:56:35.544665+00:00'
updated_at: '2023-04-10T20:23:21.423453+00:00'
---

# List all superusers

```bash
SELECT usename FROM pg_user WHERE usesuper IS TRUE
```
