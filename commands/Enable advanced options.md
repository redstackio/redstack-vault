---
id: f5a50ee5-ba87-4c8d-93ee-ca5096aa1ca8
name: Enable advanced options
type: command
executor: bash
data: "sp_configure 'show advanced options',1; \nRECONFIGURE\nGO"
output: null
created_at: '2023-04-06T03:56:20.431194+00:00'
updated_at: '2023-04-10T20:36:42.151890+00:00'
---

# Enable advanced options

```bash
sp_configure 'show advanced options',1; 
RECONFIGURE
GO
```


