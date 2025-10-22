---
id: 7fb068d2-cd1c-4259-821d-617f4bab0c4c
name: Connect to Azure Account with Access Token and Graph Token
type: command
executor: bash
data: 'PS C:\Tools> $token = <TOKEN>

  PS C:\Tools> $graphaccesstoken = <GRAPHTOKEN>

  PS C:\Tools> Connect-AzAccount -AccessToken $token -GraphAccessToken $graphaccesstoken
  -AccountId <ACCOUNT-ID>

  '
output: null
created_at: '2023-05-30T13:47:18.322998+00:00'
updated_at: '2023-05-30T13:47:19.298036+00:00'
---

# Connect to Azure Account with Access Token and Graph Token

```bash
PS C:\Tools> $token = <TOKEN>
PS C:\Tools> $graphaccesstoken = <GRAPHTOKEN>
PS C:\Tools> Connect-AzAccount -AccessToken $token -GraphAccessToken $graphaccesstoken -AccountId <ACCOUNT-ID>

```
