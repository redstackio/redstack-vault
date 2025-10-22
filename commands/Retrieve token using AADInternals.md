---
id: 80056f84-8ffc-45a7-be82-cd5a5ebb39ed
name: Retrieve token using AADInternals
type: command
executor: bash
data: 'Install-Module AADInternals -Scope CurrentUser

  Import-Module AADInternals

  $token = (Get-AADIntAccessToken -ClientId "9bc3ab49-b65d-410a-85ad-de819febfddc"
  -Tenant "your.onmicrosoft.com" -Resource "https://your.sharepoint.com")'
output: null
created_at: '2023-04-06T03:56:28.947816+00:00'
updated_at: '2023-04-10T20:37:31.881047+00:00'
---

# Retrieve token using AADInternals

```bash
Install-Module AADInternals -Scope CurrentUser
Import-Module AADInternals
$token = (Get-AADIntAccessToken -ClientId "9bc3ab49-b65d-410a-85ad-de819febfddc" -Tenant "your.onmicrosoft.com" -Resource "https://your.sharepoint.com")
```
