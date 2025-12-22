---
id: 9b95ee46-b004-4d25-8631-431335a40691
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:14.585681+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - azucar
  - export
validated: true
---

# azucar-unblock-and-export-commands

## Code

```powershell
# You should use an account with at least read-permission on the assets you want to access
PS> Get-ChildItem -Recurse c:\Azucar_V10 | Unblock-File
PS> .\Azucar.ps1 -AuthMode UseCachedCredentials -Verbose -WriteLog -Debug -ExportTo PRINT
PS> .\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate C:\AzucarTest\server.pfx -ApplicationId 00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000
PS> .\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate C:\AzucarTest\server.pfx -CertFilePassword MySuperP@ssw0rd! -ApplicationId 00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000
# resolve the TenantID for an specific username
PS> .\Azucar.ps1 -ResolveTenantUserName user@company.com
```

## Description

Sequence of Azucar commands: unblock files, export with cached/certificate auth, and resolve TenantID. Analyzes subscriptions for security risks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| c:\Azucar_V10 | Azucar directory | Adjust path |
| C:\AzucarTest\server.pfx | Cert path | server.pfx |
| MySuperP@ssw0rd! | Cert password | Change to actual |
| 00000000-... | App/Tenant IDs | Use real GUIDs |
| user@company.com | Username for resolve | target@domain.com |

## Usage

Run in PowerShell from Azucar directory. Start with unblock, then export based on auth method. Outputs risks like open ports or weak RBAC.

## Detection

- Execution of Azucar.ps1 in logs.
- API calls to Azure RM with broad read scopes.
- File creation of CSV/JSON exports with sensitive configs.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/Azucar]]
