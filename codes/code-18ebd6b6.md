---
id: 18ebd6b6-8a83-4ad4-b316-6db7b714b7af
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:15.955573+00:00'
updated_at: '2023-04-10T20:19:36.290417+00:00'
---

# Code Snippet 18ebd6b6

**Language**: Powershell

```powershell
# Enumerate possible endpoints for applications starting/ending with PREFIX
PS C:\Tools> Get-AzureADServicePrincipal -All $true -Filter "startswith(displayName,'PREFIX')" | % {$_.ReplyUrls}
PS C:\Tools> Get-AzureADApplication -All $true -Filter "endswith(displayName,'PREFIX')" | Select-Object ReplyUrls,WwwHomePage,HomePage
```
