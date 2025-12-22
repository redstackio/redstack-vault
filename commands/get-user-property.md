---
id: e5729cc3-e7a4-4ec9-9d9f-8bda607f3527
type: command
executor: powershell
data: Get-UserProperty
output: null
created_at: '2023-04-06T03:56:02.229134+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get User Property

## Command

```powershell
Get-UserProperty
```

## Description

Retrieves general user properties from the domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Default properties | No |

## Examples

### Basic Usage

```powershell
Get-UserProperty
```

## Expected Output

User property data.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
