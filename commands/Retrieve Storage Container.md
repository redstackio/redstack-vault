---
id: 6534ab4b-4514-4d35-97be-e2621fd3677d
name: Retrieve Storage Container
type: command
executor: bash
data: Get-AzStorageContainer -Context (Get-AzStorageAccount -name <NAME> -ResourceGroupName
  <NAME>).context
output: null
created_at: '2023-05-24T22:41:39.564909+00:00'
updated_at: '2023-05-24T22:41:39.704807+00:00'
---

# Retrieve Storage Container

```bash
Get-AzStorageContainer -Context (Get-AzStorageAccount -name <NAME> -ResourceGroupName <NAME>).context
```


