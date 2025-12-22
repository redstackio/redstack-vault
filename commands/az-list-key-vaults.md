---
id: 958ff107-87fd-4eae-96db-31f6047bd6d5
name: az-list-key-vaults
type: command
executor: bash
data: az keyvault list
output: null
created_at: '2023-05-25T04:48:48.223252+00:00'
updated_at: '2023-05-25T04:48:49.579271+00:00'
platforms:
  - Cloud
tags:
  - az-cli
  - enumeration
verified: true
validated: true
---

# az-list-key-vaults

## Command

```bash
az keyvault list
```

## Description

This command enumerates all Azure Key Vaults in the current subscription, revealing secret storage locations that may contain sensitive data like API keys or certificates.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Lists all key vaults with default JSON output | N/A |

## Examples

### Basic Usage

```bash
az keyvault list
```

### Advanced Usage

Output as table:
```bash
az keyvault list -o table
```

## Expected Output

JSON array example:
```
[
  {
    "id": "/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.KeyVault/vaults/myVault",
    "location": "East US",
    "name": "myVault",
    "properties": {
      "accessPolicies": [...],
      "sku": {
        "family": "vault",
        "name": "standard"
      },
      "tenantId": "xxx"
    },
    "resourceGroup": "myRG",
    "type": "Microsoft.KeyVault/vaults"
  }
]
```

## Related

- [[procedures/Azure-Tenant-Enumeration-with-Az-CLI]]
- [[tools/Azure-CLI]]
