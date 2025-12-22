---
id: d8d0e468-058f-44ec-97ac-a455505d9c3d
type: command
executor: bash
data: az login -u $_USERNAME -p $_PASSWORD
output: null
created_at: '2023-04-06T03:56:14.585576+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - auth
  - azure-cli
verified: true
validated: true
---

# azure-cli-login-with-credentials

## Command

```bash
az login -u $_USERNAME -p $_PASSWORD
```

## Description

Logs into Azure CLI using username and password for subsequent commands.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u, $_USERNAME | Username | Yes |
| -p, $_PASSWORD | Password | Yes |

## Examples

### Basic Usage

```bash
az login -u test@contoso.onmicrosoft.com -p MyPassword
```

## Expected Output

JSON with subscriptions; "Logged in successfully".

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/Azure-StormSpotter]]
