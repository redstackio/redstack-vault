---
id: 42199275-bf72-451c-a6ce-e48f6c452426
name: get-azresource
type: command
executor: powershell
data: Get-AzResource
output: null
created_at: '2023-05-30T13:47:18.323189+00:00'
updated_at: '2023-05-30T13:47:19.298036+00:00'
platforms:
  - Windows
tags:
  - cloud-enum
  - azure
verified: true
validated: true
---

# get-azresource

## Command

```powershell
Get-AzResource
```

## Description

Retrieves a list of all Azure resources accessible to the authenticated account, useful for enumerating the cloud environment post-authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (None) | Lists all resources in the current subscription context | No |

## Examples

### Basic Usage

```powershell
Get-AzResource | Format-Table Name, ResourceType, Location
```

### Advanced Usage

Filter by type:

```powershell
Get-AzResource -ResourceType 'Microsoft.Compute/virtualMachines'
```

## Expected Output

Table format:
```
Name                  ResourceType                    Location
----                  ------------                    --------
myVM                  Microsoft.Compute/virtualMachines eastus
mystorage             Microsoft.Storage/storageAccounts eastus
```
Empty if no permissions; indicates successful enum on populated output.

## Related

- [[commands/connect-azaccount-with-access-token]]
- [[procedures/Authenticate-to-Azure-Using-Managed-Identity-Access-Tokens]]
