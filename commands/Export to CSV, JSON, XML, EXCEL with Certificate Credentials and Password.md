---
id: e2490ce3-5579-458d-8e8d-4ef3a4b38c94
name: Export to CSV, JSON, XML, EXCEL with Certificate Credentials and Password
type: command
executor: bash
data: .\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials
  -Certificate C:\AzucarTest\server.pfx -CertFilePassword MySuperP@ssw0rd! -ApplicationId
  00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000
output: null
created_at: '2023-04-06T03:56:14.585956+00:00'
updated_at: '2023-04-10T20:19:39.807633+00:00'
---

# Export to CSV, JSON, XML, EXCEL with Certificate Credentials and Password

```bash
.\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate C:\AzucarTest\server.pfx -CertFilePassword MySuperP@ssw0rd! -ApplicationId 00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000
```


