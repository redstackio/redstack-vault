---
id: eede380e-1fcb-47f7-af28-70d3abcd9135
type: code
language: Powershell
verified: false
created_at: '2023-05-25T04:47:37.982500+00:00'
updated_at: '2023-05-25T04:48:03.302332+00:00'
---

# Code Snippet eede380e

**Language**: Powershell

```powershell
# Login to Azure
PS> az login -u test@<TENANT NAME>.onmicrosoft.com -p <PASSWORD>

# list all virtual machines in the current subscription
PS> az vm list

# List only the names of all virtual machines in the current subscription
az vm list --query "[].[name]" -o table

# List only names of all web apps in the current subscription
az webapp list
# List only names of all function apps in the current subscription
az functionapp list --query "[].[name]" -o table

#  Lists all storage accounts in the current subscription.
az storage account list

# Lists all key vaults in the current subscription.
az keyvault list
```


