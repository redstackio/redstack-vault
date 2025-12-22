---
id: 2bb83228-9bd1-4002-8aa4-26106160e536
name: az-list-function-app-names
type: command
executor: bash
data: 'az functionapp list --query "[].[name]" -o table'
output: null
created_at: '2023-05-25T04:48:48.222965+00:00'
updated_at: '2023-05-25T04:48:49.579271+00:00'
platforms:
  - Cloud
tags:
  - az-cli
  - enumeration
verified: true
validated: true
---

# az-list-function-app-names

## Command

```bash
az functionapp list --query "[].[name]" -o table
```

## Description

This command lists only the names of all Azure Function Apps in the current subscription, providing a quick inventory of serverless resources without full details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --query "[].[name]" | JMESPath query to extract only the 'name' field from each function app | Yes |
| -o, --output table | Format output as a table for readability | Yes |

## Examples

### Basic Usage

```bash
az functionapp list --query "[].[name]" -o table
```

### Advanced Usage

Filter by resource group:
```bash
az functionapp list --resource-group $_RESOURCE_GROUP --query "[].[name]" -o table
```

## Expected Output

```
Name
------------
myfunctionapp1
myfunctionapp2
```

Empty table if no function apps exist.

## Related

- [[procedures/Azure-Tenant-Enumeration-with-Az-CLI]]
- [[tools/Azure-CLI]]
