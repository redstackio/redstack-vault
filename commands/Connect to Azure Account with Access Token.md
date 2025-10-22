---
id: a3bf5def-a02e-44f4-bcd3-75a5876eb51b
name: Connect to Azure Account with Access Token
type: command
executor: bash
data: 'PS C:\Tools> $token = ''eyJ0e..''

  PS C:\Tools> Connect-AzAccount -AccessToken $token -AccountId <ACCOUNT-ID>

  '
output: null
created_at: '2023-05-30T13:47:18.322713+00:00'
updated_at: '2023-05-30T13:47:19.298036+00:00'
---

# Connect to Azure Account with Access Token

```bash
PS C:\Tools> $token = 'eyJ0e..'
PS C:\Tools> Connect-AzAccount -AccessToken $token -AccountId <ACCOUNT-ID>

```
