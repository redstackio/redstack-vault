---
id: fc15e621-6e4a-4f3f-bf5d-108f933be6cf
name: Encrypt connection strings
type: command
executor: bash
data: aspnet_regiis -pdf "connectionStrings" "." -prov "DataProtectionConfigurationProvider"
output: null
created_at: '2023-04-06T03:55:51.711373+00:00'
updated_at: '2023-04-10T20:21:11.234187+00:00'
---

# Encrypt connection strings

```bash
aspnet_regiis -pdf "connectionStrings" "." -prov "DataProtectionConfigurationProvider"
```
