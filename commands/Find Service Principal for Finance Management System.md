---
id: ad793b05-8156-416b-b436-8ac485e85b2b
name: Find Service Principal for Finance Management System
type: command
executor: bash
data: Get-AzureADServicePrincipal -All $true | ?{$_.DisplayName -eq "Finance Management
  System"}
output: null
created_at: '2023-04-06T03:56:15.918844+00:00'
updated_at: '2023-04-10T20:19:39.400527+00:00'
---

# Find Service Principal for Finance Management System

```bash
Get-AzureADServicePrincipal -All $true | ?{$_.DisplayName -eq "Finance Management System"}
```
