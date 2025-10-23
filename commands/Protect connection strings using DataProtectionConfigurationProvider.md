---
id: 396b67a2-2fc7-4a12-8247-7d01820b0d86
name: Protect connection strings using DataProtectionConfigurationProvider
type: command
executor: bash
data: aspnet_regiis -pdf "connectionStrings" "." -prov "DataProtectionConfigurationProvider"
output: null
created_at: '2023-04-06T03:55:53.343152+00:00'
updated_at: '2023-04-06T03:55:53.350236+00:00'
---

# Protect connection strings using DataProtectionConfigurationProvider

```bash
aspnet_regiis -pdf "connectionStrings" "." -prov "DataProtectionConfigurationProvider"
```


