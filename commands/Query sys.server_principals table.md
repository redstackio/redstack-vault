---
id: c0c54e93-5e9a-415e-8ad5-aaa671a7be10
name: Query sys.server_principals table
type: command
executor: bash
data: Select * from sys.server_principals where type_desc != 'SERVER_ROLE'
output: null
created_at: '2023-04-06T03:56:20.842671+00:00'
updated_at: '2023-04-10T20:36:42.877343+00:00'
---

# Query sys.server_principals table

```bash
Select * from sys.server_principals where type_desc != 'SERVER_ROLE'
```
