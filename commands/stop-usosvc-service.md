---
id: 40307738-ba76-4a1d-8260-42535f453808
name: Stop UsoSvc service
type: command
executor: cmd
data: sc.exe stop UsoSvc
output: null
created_at: '2023-04-06T03:56:29.494693+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - service-management
verified: true
validated: true
---

# Stop UsoSvc Service

## Command

```cmd
sc.exe stop UsoSvc
```

## Description

This command stops the Update Orchestrator Service (UsoSvc) on a Windows system, which is required before reconfiguring its binary path for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `stop` | Operation to halt the service | Yes |
| `UsoSvc` | Name of the service to stop | Yes |

## Examples

### Basic Usage

```cmd
sc.exe stop UsoSvc
```

### With Error Handling

Run in an elevated or low-priv prompt; errors may occur if service is not running.

## Expected Output

SERVICE_NAME: UsoSvc
        TYPE               : 20  WIN32_SHARE_PROCESS
        ... (service details)

[SC] ControlService SUCCESS

Or error if already stopped: [SC] ControlService FAILED 1056: The requested control is not valid for this service.

## Related

- [[procedures/usosvc-service-account-remote-command-execution]]
- [[commands/start-usosvc-service]]
