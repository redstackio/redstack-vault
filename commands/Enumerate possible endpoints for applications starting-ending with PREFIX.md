---
id: 29fb9e2a-c595-4cf7-bb0b-848c2e95ef36
name: Enumerate possible endpoints for applications starting/ending with PREFIX
type: command
executor: bash
data: 'Get-AzureADServicePrincipal -All $true -Filter "startswith(displayName,''PREFIX'')"
  | % {$_.ReplyUrls}

  Get-AzureADApplication -All $true -Filter "endswith(displayName,''PREFIX'')" | Select-Object
  ReplyUrls,WwwHomePage,HomePage'
output: null
created_at: '2023-04-06T03:56:15.955621+00:00'
updated_at: '2023-04-10T20:19:36.288548+00:00'
---

# Enumerate possible endpoints for applications starting/ending with PREFIX

```bash
Get-AzureADServicePrincipal -All $true -Filter "startswith(displayName,'PREFIX')" | % {$_.ReplyUrls}
Get-AzureADApplication -All $true -Filter "endswith(displayName,'PREFIX')" | Select-Object ReplyUrls,WwwHomePage,HomePage
```


