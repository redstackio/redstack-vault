---
type: command
executor: powershell
data: 'Get-AzWebApp | Where-Object {$_.Kind -notmatch "functionapp"}'
output: null
platforms:
  - Cloud
tags:
  - az-powershell
  - enumeration
  - web
verified: true
validated: true
---

# Get-Az Web App Exclude Functions

## Command

```powershell
Get-AzWebApp | Where-Object {$_.Kind -notmatch "functionapp"}
```

## Description

This command lists Azure App Service web apps, excluding Function Apps via filtering. Use to focus on traditional web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ResourceGroupName | Filter by resource group | No |
| Where-Object | PowerShell filter to exclude Kind matching 'functionapp' | Built-in |

## Examples

### Basic Usage

```powershell
Get-AzWebApp | Where-Object {$_.Kind -notmatch "functionapp"}
```

### Advanced Usage

With export:

```powershell
Get-AzWebApp | Where-Object {$_.Kind -notmatch "functionapp"} | Export-Csv webapps.csv
```

## Expected Output

Table:

```
Name      State    Location
----      -----    --------
mywebapp  Running  eastus
```

## Related

- [[Azure Tenant Enumeration with Az PowerShell (Creds)]
- [[commands/get-az-function-app]]
