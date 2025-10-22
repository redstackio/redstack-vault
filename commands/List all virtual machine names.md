---
id: 712d3939-d52b-4e68-9b84-8b96b6e5421c
name: List all virtual machine names
type: command
executor: bash
data: az vm list --query "[].[name]" -o table
output: null
created_at: '2023-05-25T04:48:48.222786+00:00'
updated_at: '2023-05-25T04:48:49.579271+00:00'
---

# List all virtual machine names

```bash
az vm list --query "[].[name]" -o table
```
