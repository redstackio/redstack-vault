---
id: 2bb83228-9bd1-4002-8aa4-26106160e536
name: List all function app names
type: command
executor: bash
data: az functionapp list --query "[].[name]" -o table
output: null
created_at: '2023-05-25T04:48:48.222965+00:00'
updated_at: '2023-05-25T04:48:49.579271+00:00'
---

# List all function app names

```bash
az functionapp list --query "[].[name]" -o table
```
