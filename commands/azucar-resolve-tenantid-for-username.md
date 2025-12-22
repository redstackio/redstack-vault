---
id: 6adadaef-63e9-42ba-87ab-d173f7b6de01
type: command
executor: powershell
data: .\Azucar.ps1 -ResolveTenantUserName $_USERNAME
output: null
created_at: '2023-04-06T03:56:14.585979+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - tenant
  - resolve
verified: true
validated: true
---

# azucar-resolve-tenantid-for-username

## Command

```powershell
.\Azucar.ps1 -ResolveTenantUserName $_USERNAME
```

## Description

Resolves the Tenant ID for a given username using Azucar.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ResolveTenantUserName, $_USERNAME | Email/username | Yes |

## Examples

### Basic Usage

```powershell
.\Azucar.ps1 -ResolveTenantUserName user@company.com
```

## Expected Output

Tenant ID printed to console.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/Azucar]]
