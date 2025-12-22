---
id: 896ae488-f19e-419f-b450-d7492bdcf49f
name: list-owned-objects-in-azure-ad
type: command
executor: bash
data: az ad signed-in-user list-owned-objects
output: null
created_at: '2023-05-24T22:50:53.198584+00:00'
updated_at: '2023-05-24T22:50:54.391095+00:00'
platforms:
  - Cloud
tags:
  - azure
  - discovery
verified: true
validated: true
---

# list-owned-objects-in-azure-ad

## Command

```bash
az ad signed-in-user list-owned-objects
```

## Description

This Azure CLI command lists Azure AD objects owned by the signed-in user, such as groups or apps, to identify resources for privilege escalation in Automation contexts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Queries for the current signed-in user | N/A |

## Examples

### Basic Usage

```bash
az ad signed-in-user list-owned-objects
```

### Advanced Usage

Query specific type: az ad signed-in-user list-owned-objects --query "[?@odata.type=='#microsoft.graph.group']"

## Expected Output

JSON array of owned objects, e.g., [{"@odata.type": "#microsoft.graph.group", "id": "group-id", "displayName": "Automation Admins"}].

## Related

- [[procedures/Create-and-Execute-Malicious-Azure-Runbook]]
- [[commands/add-user-to-automation-admins-group]]
