---
id: 9b95ee46-b004-4d25-8631-431335a40691
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:14.585681+00:00'
updated_at: '2023-04-10T20:19:39.811529+00:00'
---

# Code Snippet 9b95ee46

**Language**: Powershell

```powershell
# You should use an account with at least read-permission on the assets you want to access
PS> Get-ChildItem -Recurse c:\Azucar_V10 | Unblock-File
PS> .\Azucar.ps1 -AuthMode UseCachedCredentials -Verbose -WriteLog -Debug -ExportTo PRINT
PS> .\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate C:\AzucarTest\server.pfx -ApplicationId 00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000
PS> .\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate C:\AzucarTest\server.pfx -CertFilePassword MySuperP@ssw0rd! -ApplicationId 00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000
# resolve the TenantID for an specific username
PS> .\Azucar.ps1 -ResolveTenantUserName user@company.com
```


