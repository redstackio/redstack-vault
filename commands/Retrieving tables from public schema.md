---
id: 9d6a4fde-0fd2-48ba-840c-ef207a0010d8
name: Retrieving tables from public schema
type: command
executor: bash
data: SELECT * FROM information_schema.tables WHERE table_schema = 'public';
output: null
created_at: '2023-04-06T03:56:36.832375+00:00'
updated_at: '2023-04-10T20:24:24.386328+00:00'
---

# Retrieving tables from public schema

```bash
SELECT * FROM information_schema.tables WHERE table_schema = 'public';
```


