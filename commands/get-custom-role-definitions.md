---
id: 2c807040-6354-45f4-8fa0-e911679454f6
name: get-custom-role-definitions
type: command
executor: powershell
data: >-
  Get-AzureADMSRoleDefinition | Where-Object {$_.IsBuiltin -eq $False} |
  Select-Object DisplayName
output: null
created_at: '2023-05-23T19:33:22.168801+00:00'
updated_at: '2023-05-23T19:33:22.785549+00:00'
platforms:
  - Cloud
tags:
  - azure-ad
  - enumeration
  - roles
verified: true
validated: true
---

# Get Custom Role Definitions

## Command

```powershell
Get-AzureADMSRoleDefinition | Where-Object {$_.IsBuiltin -eq $False} | Select-Object DisplayName
```

## Description

Fetches all custom (non-built-in) Microsoft Entra role definitions to reveal tenant-specific permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Where-Object | Filters out built-in roles | Built-in |
| $_.IsBuiltin -eq $False | Condition for custom roles | Built-in |
| Select-Object | Projects display name | Built-in |

## Examples

### Basic Usage

```powershell
Get-AzureADMSRoleDefinition | Where-Object {$_.IsBuiltin -eq $False} | Select-Object DisplayName
```

### Advanced Usage

Include description: ... | Select-Object DisplayName, Description

## Expected Output

DisplayName
-----------
Custom IT Support Role
Custom Security Auditor

## Related

- [[procedures/azure-ad-enumeration-using-powershell-with-credentials]]
