---
id: 2c807040-6354-45f4-8fa0-e911679454f6
name: Get all custom role definitions
type: command
executor: bash
data: Get-AzureADMSRoleDefinition | ?{$_.IsBuiltin -eq $False} | select DisplayName
output: null
created_at: '2023-05-23T19:33:22.168801+00:00'
updated_at: '2023-05-23T19:33:22.785549+00:00'
---

# Get all custom role definitions

```bash
Get-AzureADMSRoleDefinition | ?{$_.IsBuiltin -eq $False} | select DisplayName
```


