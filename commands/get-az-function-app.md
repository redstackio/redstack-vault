---
type: command
executor: powershell
data: Get-AzFunctionApp
output: null
platforms:
  - Cloud
tags:
  - az-powershell
  - enumeration
  - serverless
verified: true
validated: true
---

# Get-Az Function App

## Command

```powershell
Get-AzFunctionApp
```

## Description

This command lists Azure Function Apps. Use for discovering serverless compute resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Name | Specific function app name | No |
| -ResourceGroupName | Filter by resource group | No |

## Examples

### Basic Usage

```powershell
Get-AzFunctionApp
```

### Advanced Usage

Detailed view:

```powershell
Get-AzFunctionApp | Format-List
```

## Expected Output

Table:

```
Name             Location
----             --------
myfunctionapp    eastus
```

## Related

- [[Azure Tenant Enumeration with Az PowerShell (Creds)]
- [[commands/get-az-web-app-exclude-functions]]
