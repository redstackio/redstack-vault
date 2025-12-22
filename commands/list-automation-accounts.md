---
id: 7680b0d9-dc8d-4fa8-9c54-9f18c8e12394
name: list-automation-accounts
type: command
executor: bash
data: az automation account list
output: null
created_at: '2023-05-24T22:50:53.197507+00:00'
updated_at: '2023-05-24T22:50:54.391095+00:00'
platforms:
  - Cloud
tags:
  - azure
  - discovery
verified: true
validated: true
---

# list-automation-accounts

## Command

```bash
az automation account list
```

## Description

This Azure CLI command lists all Automation Accounts accessible to the signed-in user, providing an overview of potential targets for runbook automation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Lists all accounts in the current subscription | N/A |

## Examples

### Basic Usage

```bash
az automation account list
```

### Advanced Usage

Filter output: az automation account list --query "[?name=='MyAccount']"

## Expected Output

JSON array of accounts, e.g., [{"name": "MyAccount", "resourceGroup": "MyRG", "location": "East US"}]. Empty array indicates no access.

## Related

- [[procedures/Create-and-Execute-Malicious-Azure-Runbook]]
- [[commands/check-user-rights-for-automation]]
