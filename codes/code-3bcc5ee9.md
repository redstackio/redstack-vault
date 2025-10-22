---
id: 3bcc5ee9-012b-42e9-b383-5a15661878c5
type: code
language: Powershell
verified: false
created_at: '2023-05-23T19:30:12.768706+00:00'
updated_at: '2023-05-25T04:47:38.094303+00:00'
---

# Code Snippet 3bcc5ee9

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
