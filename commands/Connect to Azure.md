---
id: 4902a1ba-1e85-42c9-b898-eae6c01d4a6d
name: Connect to Azure
type: command
executor: bash
data: 'PS> $token = ''eyJ0..''


  PS> $keyvaulttoken = ''eyJ0..''


  PS Az> Connect-AzAccount -AccessToken $token -AccountId 2e91a4fea0f2-46ee-8214-fa2ff6aa9abc
  -KeyVaultAccessToken $keyvaulttoken'
output: null
created_at: '2023-05-24T18:03:17.783443+00:00'
updated_at: '2023-05-24T18:03:18.179034+00:00'
---

# Connect to Azure

```bash
PS> $token = 'eyJ0..'

PS> $keyvaulttoken = 'eyJ0..'

PS Az> Connect-AzAccount -AccessToken $token -AccountId 2e91a4fea0f2-46ee-8214-fa2ff6aa9abc -KeyVaultAccessToken $keyvaulttoken
```


