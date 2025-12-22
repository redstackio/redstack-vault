---
id: eef95608-557b-4bc0-a810-5710411c884b
type: command
executor: powershell
data: Get-Resources
output: null
created_at: '2023-04-06T03:56:14.586556+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
tags:
  - resources
  - enum
verified: true
validated: true
---

# powerzure-get-resources

## Command

```powershell
Get-Resources
```

## Description

Enumerates all resources in the current Azure subscription.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses current context | No |

## Examples

### Basic Usage

```powershell
Get-Resources
```

## Expected Output

List of resources with types and locations.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/PowerZure]]
