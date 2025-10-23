---
id: 88473a7c-f85b-45c1-8fb4-94565bb7bd91
name: Get Key Vault Access Token
type: command
executor: bash
data: 'curl "$IDENTITY_ENDPOINT?resource=https://vault.azure.net&apiversion=2017-09-01"
  -H secret:$IDENTITY_HEADER

  curl "$IDENTITY_ENDPOINT?resource=https://management.azure.com&apiversion=2017-09-01"
  -H secret:$IDENTITY_HEADER'
output: null
created_at: '2023-05-24T18:03:17.782961+00:00'
updated_at: '2023-05-24T18:03:18.179034+00:00'
---

# Get Key Vault Access Token

```bash
curl "$IDENTITY_ENDPOINT?resource=https://vault.azure.net&apiversion=2017-09-01" -H secret:$IDENTITY_HEADER
curl "$IDENTITY_ENDPOINT?resource=https://management.azure.com&apiversion=2017-09-01" -H secret:$IDENTITY_HEADER
```


