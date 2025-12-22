---
id: e45f2de3-b356-4bd3-878a-972e2f7a4785
name: az-list-web-apps
type: command
executor: bash
data: az webapp list
output: null
created_at: '2023-05-25T04:48:48.222894+00:00'
updated_at: '2023-05-25T04:48:49.579271+00:00'
platforms:
  - Cloud
tags:
  - az-cli
  - enumeration
verified: true
validated: true
---

# az-list-web-apps

## Command

```bash
az webapp list
```

## Description

This command enumerates all web apps in the subscription, useful for discovering hosted applications that may have vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Lists all web apps in JSON | N/A |

## Examples

### Basic Usage

```bash
az webapp list
```

### Advanced Usage

Table format:
```bash
az webapp list -o table
```

## Expected Output

JSON example:
```
[
  {
    "defaultHostName": "mywebapp.azurewebsites.net",
    "id": "/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Web/sites/mywebapp",
    "kind": "app",
    "location": "East US",
    "name": "mywebapp",
    "state": "Running",
    "type": "Microsoft.Web/sites"
  }
]
```

## Related

- [[procedures/Azure-Tenant-Enumeration-with-Az-CLI]]
- [[tools/Azure-CLI]]
