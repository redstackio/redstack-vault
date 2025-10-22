---
id: 0904e875-6ef0-4637-a3cc-a814e86beeef
name: Retrieve user information from PostgreSQL database
type: command
executor: bash
data: SELECT usename, usecreatedb, usesuper, usecatupd FROM pg_user
output: null
created_at: '2023-04-06T03:56:35.569010+00:00'
updated_at: '2023-04-10T20:23:16.886765+00:00'
---

# Retrieve user information from PostgreSQL database

```bash
SELECT usename, usecreatedb, usesuper, usecatupd FROM pg_user
```
