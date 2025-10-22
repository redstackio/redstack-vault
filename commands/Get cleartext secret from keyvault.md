---
id: d190bc08-76be-4991-b13d-4e5b90d007f4
name: Get cleartext secret from keyvault
type: command
executor: bash
data: 'az keyvault secret show --id <URI from last command> | ConvertFrom-Json

  '
output: null
created_at: '2020-07-14T19:07:50.930046+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get cleartext secret from keyvault

```bash
az keyvault secret show --id <URI from last command> | ConvertFrom-Json

```
