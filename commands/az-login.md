---
data: az login
tags:
  - azure
  - auth
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:01.967Z'
id: d94773d4-f857-4d75-88ba-7f2bf44867de
verified: false
validated: true
submitted: true
---
# az-login

## Command

```bash
az login
```

## Description

Authenticates to Azure CLI for resource management, required before creating App Services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Interactive login | Yes |

## Examples

### Basic Usage

```bash
az login
```

### Advanced Usage

```bash
az login --service-principal -u client_id -p secret --tenant tenant_id
```

## Expected Output

JSON with subscriptions; select one.

## Related

- [[commands/az-webapp-create]]
