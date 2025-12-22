---
id: 712d3939-d52b-4e68-9b84-8b96b6e5421c
name: az-list-vm-names
type: command
executor: bash
data: 'az vm list --query "[].[name]" -o table'
output: null
created_at: '2023-05-25T04:48:48.222786+00:00'
updated_at: '2023-05-25T04:48:49.579271+00:00'
platforms:
  - Cloud
tags:
  - az-cli
  - enumeration
verified: true
validated: true
---

# az-list-vm-names

## Command

```bash
az vm list --query "[].[name]" -o table
```

## Description

This command retrieves only the names of all virtual machines in the subscription, offering a streamlined list for targeting specific instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --query "[].[name]" | JMESPath query to select only VM names | Yes |
| -o, --output table | Display as a table | Yes |

## Examples

### Basic Usage

```bash
az vm list --query "[].[name]" -o table
```

### Advanced Usage

By resource group:
```bash
az vm list --resource-group $_RESOURCE_GROUP --query "[].[name]" -o table
```

## Expected Output

```
Name
------------
myvm1
myvm2
```

## Related

- [[procedures/Azure-Tenant-Enumeration-with-Az-CLI]]
- [[tools/Azure-CLI]]
