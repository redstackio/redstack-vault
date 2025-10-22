---
id: 677cc791-aa32-4c2f-8322-0ae64be83575
name: Generate RDS DB Auth Token
type: command
executor: bash
data: TOKEN=$(aws rds generate-db-auth-token --hostname hostname --port port --username
  username --region region)
output: null
created_at: '2023-04-06T03:56:14.073780+00:00'
updated_at: '2023-04-10T20:20:55.168825+00:00'
---

# Generate RDS DB Auth Token

```bash
TOKEN=$(aws rds generate-db-auth-token --hostname hostname --port port --username username --region region)
```
