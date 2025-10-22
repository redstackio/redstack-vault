---
id: efff92ef-b55a-4d89-af63-cc7edd0e7b3a
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:15.011945+00:00'
updated_at: '2023-05-23T19:29:58.823366+00:00'
---

# Code Snippet efff92ef

**Language**: Powershell

```powershell
PS> az login -u test@<TENANT NAME>.onmicrosoft.com -p <PASSWORD>

Commands:
- az vm list: Lists all virtual machines in the current subscription.
- az vm list --query "[].[name]" -o table: Lists only the names of all virtual machines in the current subscription.
- az webapp list: Lists all web apps in the current subscription.
- az functionapp list --query "[].[name]" -o table: Lists only the names of all function apps in the current subscription.
- az storage account list: Lists all storage accounts in the current subscription.
- az keyvault list: Lists all key vaults in the current subscription.
```
