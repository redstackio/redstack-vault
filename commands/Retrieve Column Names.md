---
id: 823b11b5-35b4-47b6-8512-81e4adf9f56f
name: Retrieve Column Names
type: command
executor: bash
data: SELECT column_name FROM information_schema.columns WHERE table_name='data_table'
output: null
created_at: '2023-04-06T03:56:35.720094+00:00'
updated_at: '2023-04-10T20:23:22.506826+00:00'
---

# Retrieve Column Names

```bash
SELECT column_name FROM information_schema.columns WHERE table_name='data_table'
```
