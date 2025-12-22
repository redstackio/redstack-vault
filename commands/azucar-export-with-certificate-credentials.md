---
id: b69260b3-9c9f-4635-aea8-6f327972ad08
type: command
executor: powershell
data: >-
  .\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials
  -Certificate $_CERT_PATH -ApplicationId $_APP_ID -TenantID $_TENANT_ID
output: null
created_at: '2023-04-06T03:56:14.585856+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - export
  - azure
verified: true
validated: true
---

# azucar-export-with-certificate-credentials

## Command

```powershell
.\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate $_CERT_PATH -ApplicationId $_APP_ID -TenantID $_TENANT_ID
```

## Description

Exports Azure subscription data to multiple formats using certificate-based authentication with Azucar.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ExportTo | Formats: CSV,JSON,XML,EXCEL | Yes |
| -AuthMode | Certificate_Credentials | Yes |
| -Certificate, $_CERT_PATH | Path to .pfx certificate | Yes |
| -ApplicationId, $_APP_ID | App ID for service principal | Yes |
| -TenantID, $_TENANT_ID | Tenant GUID | Yes |

## Examples

### Basic Usage

```powershell
.\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate C:\AzucarTest\server.pfx -ApplicationId 00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000
```

## Expected Output

Files exported to current directory with risk analysis data.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/Azucar]]
