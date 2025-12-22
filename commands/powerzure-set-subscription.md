---
id: 774df0ae-e18e-491f-a55f-312fd8eaa1da
type: command
executor: powershell
data: Set-Subscription -Id $_SUB_ID
output: null
created_at: '2023-04-06T03:56:14.586441+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
tags:
  - subscription
  - set
verified: true
validated: true
---

# powerzure-set-subscription

## Command

```powershell
Set-Subscription -Id $_SUB_ID
```

## Description

Sets the active Azure subscription for PowerZure operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Id, $_SUB_ID | Subscription ID or name | Yes |

## Examples

### Basic Usage

```powershell
Set-Subscription -Id [idgoeshere]
```

## Expected Output

"Subscription set to [name]".

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/PowerZure]]
