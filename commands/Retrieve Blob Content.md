---
id: d3117f69-f1f3-4c59-bc07-a1f6c9b21626
name: Retrieve Blob Content
type: command
executor: bash
data: Get-AzStorageBlobContent -Container <NAME> -Context (Get-AzStorageAccount -name
  <NAME> -ResourceGroupName <NAME>).context -Blob
output: null
created_at: '2023-05-24T22:41:39.565569+00:00'
updated_at: '2023-05-24T22:41:39.704807+00:00'
---

# Retrieve Blob Content

```bash
Get-AzStorageBlobContent -Container <NAME> -Context (Get-AzStorageAccount -name <NAME> -ResourceGroupName <NAME>).context -Blob
```
