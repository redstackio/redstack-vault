---
id: 6741aa9e-2692-4b5a-9e15-8e0bed3a7541
type: command
executor: powershell
data: >-
  .\Azucar.ps1 -AuthMode UseCachedCredentials -Verbose -WriteLog -Debug
  -ExportTo PRINT
output: null
created_at: '2023-04-06T03:56:14.585793+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - export
  - azure
verified: true
validated: true
---

# azucar-export-to-print-cached-creds

## Command

```powershell
.\Azucar.ps1 -AuthMode UseCachedCredentials -Verbose -WriteLog -Debug -ExportTo PRINT
```

## Description

Prints Azure risk assessment using cached Azure CLI credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -AuthMode | UseCachedCredentials | Yes |
| -Verbose | Enable verbose output | No |
| -WriteLog | Log to file | No |
| -Debug | Debug mode | No |
| -ExportTo | PRINT for console output | Yes |

## Examples

### Basic Usage

```powershell
.\Azucar.ps1 -AuthMode UseCachedCredentials -Verbose -WriteLog -Debug -ExportTo PRINT
```

## Expected Output

Console output with security risks and configs.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/Azucar]]
