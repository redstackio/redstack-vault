---
id: b69260b3-9c9f-4635-aea8-6f327972ad08
name: Export to CSV, JSON, XML, EXCEL with Certificate Credentials
type: command
executor: bash
data: .\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials
  -Certificate C:\AzucarTest\server.pfx -ApplicationId 00000000-0000-0000-0000-000000000000
  -TenantID 00000000-0000-0000-0000-000000000000
output: null
created_at: '2023-04-06T03:56:14.585856+00:00'
updated_at: '2023-04-10T20:19:39.807633+00:00'
---

# Export to CSV, JSON, XML, EXCEL with Certificate Credentials

```bash
.\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate C:\AzucarTest\server.pfx -ApplicationId 00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000
```
