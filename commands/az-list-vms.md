---
id: ecfa2935-e470-403c-9b89-aebfdb3924ef
name: az-list-vms
type: command
executor: bash
data: az vm list
output: null
created_at: '2023-05-25T04:48:48.222671+00:00'
updated_at: '2023-05-25T04:48:49.579271+00:00'
platforms:
  - Cloud
tags:
  - az-cli
  - enumeration
verified: true
validated: true
---

# az-list-vms

## Command

```bash
az vm list
```

## Description

This command lists all virtual machines in the current subscription, providing comprehensive details for infrastructure mapping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Full list in JSON format | N/A |

## Examples

### Basic Usage

```bash
az vm list
```

### Advanced Usage

Table output:
```bash
az vm list -o table
```

## Expected Output

JSON array example:
```
[
  {
    "id": "/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Compute/virtualMachines/myvm",
    "location": "East US",
    "name": "myvm",
    "properties": {
      "hardwareProfile": {
        "vmSize": "Standard_DS1_v2"
      },
      "provisioningState": "Succeeded",
      "storageProfile": {...}
    },
    "resourceGroup": "myRG",
    "vmId": "xxx"
  }
]
```

## Related

- [[procedures/Azure-Tenant-Enumeration-with-Az-CLI]]
- [[tools/Azure-CLI]]
