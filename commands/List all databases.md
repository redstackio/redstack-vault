---
id: 755975e1-082b-42b7-8bd1-b72474f9bf46
name: List all databases
type: command
executor: bash
data: SELECT datname FROM pg_database
output: null
created_at: '2023-04-06T03:56:35.661283+00:00'
updated_at: '2023-04-10T20:23:14.439957+00:00'
---

# List all databases

```bash
SELECT datname FROM pg_database
```
