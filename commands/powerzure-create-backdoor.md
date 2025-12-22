---
id: 0dee85b5-9e90-4ea7-b04b-09368c6a5083
type: command
executor: powershell
data: Create-Backdoor
output: null
created_at: '2023-04-06T03:56:14.587167+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
tags:
  - backdoor
  - persistence
verified: true
validated: true
---

# powerzure-create-backdoor

## Command

```powershell
Create-Backdoor
```

## Description

Creates a backdoor on an Azure VM using Owner/Administrator privileges via PowerZure, allowing persistent remote access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Assumes PowerZure imported and subscription set; targets default VM | No |

## Examples

### Basic Usage

```powershell
Create-Backdoor
```

## Expected Output

Backdoor deployed; confirmation: "Backdoor created successfully on VM".

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/PowerZure]]
