---
id: 263be7ea-84cc-4e23-b575-59c67709fd01
name: List table catalog and column names
type: command
executor: bash
data: SELECT table_catalog, column_name FROM information_schema.columns
output: null
created_at: '2023-04-06T03:56:33.676070+00:00'
updated_at: '2023-04-10T20:22:44.531078+00:00'
---

# List table catalog and column names

```bash
SELECT table_catalog, column_name FROM information_schema.columns
```
