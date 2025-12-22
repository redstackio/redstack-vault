---
id: f7dc3d77-b392-4a15-9dcb-bd76f74a92fc
type: command
executor: powershell
data: Get-AllSecrets
output: null
created_at: '2023-04-06T03:56:14.586824+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
tags:
  - secrets
  - collection
verified: true
validated: true
---

# powerzure-get-all-secrets

## Command

```powershell
Get-AllSecrets
```

## Description

Retrieves all accessible secrets from Key Vaults and App Registrations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses current subscription | No |

## Examples

### Basic Usage

```powershell
Get-AllSecrets
```

## Expected Output

List of secrets; variants: AllAppSecrets, AllKeyVaultContents.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/PowerZure]]
