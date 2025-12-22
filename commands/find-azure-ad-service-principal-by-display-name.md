---
type: command
executor: powershell
data: >-
  Get-AzureADServicePrincipal -All $true | Where-Object {$_.DisplayName -eq
  "<APPLICATION-DISPLAY-NAME>"}
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Azure AD
tags:
  - discovery
  - azure
verified: true
validated: true
---

# Find Azure AD Service Principal by Display Name

## Command

```powershell
Get-AzureADServicePrincipal -All $true | Where-Object {$_.DisplayName -eq "<APPLICATION-DISPLAY-NAME>"}
```

## Description

This command searches all Azure AD service principals for one matching the specified display name, useful for locating details of applications like those with Application Proxy.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -All | Retrieves all service principals | Yes (set to $true) |
| DisplayName | The display name to filter by (e.g., "Finance Management System") | Yes |

## Examples

### Basic Usage

```powershell
Get-AzureADServicePrincipal -All $true | Where-Object {$_.DisplayName -eq "Finance Management System"}
```

### Advanced Usage

Filter and select specific properties:

```powershell
Get-AzureADServicePrincipal -All $true | Where-Object {$_.DisplayName -eq "Finance Management System"} | Select-Object ObjectId, AppId, DisplayName
```

## Expected Output

Service principal details:

```
ObjectId                                   DisplayName             AppId
--------                                   -----------             -----
12345678-1234-1234-1234-123456789abc       Finance Management System 87654321-4321-4321-4321-cba987654321
KeyId                                      : abcdef12-3456-7890-abcd-ef1234567890
```

## Related

- [[procedures/azure-application-proxy-enumeration]]
- [[commands/enumerate-azure-ad-applications-with-proxy]]
