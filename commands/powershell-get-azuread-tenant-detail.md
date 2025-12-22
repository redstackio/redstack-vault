---
id: 1c670cdd-9400-401f-85db-1b3d585fd629
name: PowerShell Get AzureAD Tenant Detail
type: command
executor: powershell
data: Get-AzureADTenantDetail
output: null
created_at: '2023-05-23T17:02:42.395614+00:00'
updated_at: '2023-05-23T17:02:42.699898+00:00'
platforms:
  - Cloud
tags:
  - enumeration
  - azure
verified: true
validated: true
---

# PowerShell Get AzureAD Tenant Detail

## Command

```powershell
Get-AzureADTenantDetail
```

## Description

This PowerShell command retrieves detailed information about the current Azure AD tenant, including the Tenant ID, display name, and verified domains. Requires the AzureAD module and may prompt for authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses current context or prompts for login | N/A |
| -ErrorAction | Handles errors (e.g., SilentlyContinue) | No |

## Examples

### Basic Usage

```powershell
Get-AzureADTenantDetail
```

### With Error Handling

```powershell
Get-AzureADTenantDetail -ErrorAction SilentlyContinue | Select-Object ObjectId, DisplayName
```

## Expected Output

Object output like:
```
ObjectId                             DisplayName Country
--------                             ----------- -------
12345678-1234-1234-1234-123456789abc Target Org  US
```
The ObjectId is the Tenant ID GUID.

## Related

- [[procedures/Azure Tenant ID Enumeration]]
- [[commands/curl-azure-openid-config]]
