---
id: e2490ce3-5579-458d-8e8d-4ef3a4b38c94
type: command
executor: powershell
data: >-
  .\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials
  -Certificate $_CERT_PATH -CertFilePassword $_CERT_PASSWORD -ApplicationId
  $_APP_ID -TenantID $_TENANT_ID
output: null
created_at: '2023-04-06T03:56:14.585956+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - export
  - azure
verified: true
validated: true
---

# azucar-export-with-certificate-and-password

## Command

```powershell
.\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate $_CERT_PATH -CertFilePassword $_CERT_PASSWORD -ApplicationId $_APP_ID -TenantID $_TENANT_ID
```

## Description

Exports Azure data using password-protected certificate authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -CertFilePassword, $_CERT_PASSWORD | Password for .pfx file | Yes |
| Others | Same as certificate export | Yes |

## Examples

### Basic Usage

```powershell
.\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate C:\AzucarTest\server.pfx -CertFilePassword MySuperP@ssw0rd! -ApplicationId 00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000
```

## Expected Output

Exported files with subscription configs and risks.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/Azucar]]
