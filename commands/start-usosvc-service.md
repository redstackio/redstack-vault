---
id: 36fb2871-c5ae-4dca-b7a0-3e932c498609
name: Start UsoSvc service
type: command
executor: cmd
data: sc.exe start UsoSvc
output: null
created_at: '2023-04-06T03:56:29.494997+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - service-management
  - execution
verified: true
validated: true
---

# Start UsoSvc Service

## Command

```cmd
sc.exe start UsoSvc
```

## Description

Starts the UsoSvc service, triggering execution of the modified binary path for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `start` | Operation to start the service | Yes |
| `UsoSvc` | Service name | Yes |

## Examples

### Basic Usage

```cmd
sc.exe start UsoSvc
```

## Expected Output

[SC] StartService SUCCESS

Or details on service startup.

## Related

- [[procedures/usosvc-service-account-remote-command-execution]]
- [[commands/stop-usosvc-service]]
