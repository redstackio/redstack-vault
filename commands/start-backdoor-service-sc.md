---
id: 2aefb882-c789-4986-8fba-17bd31ba106d
name: start-backdoor-service-sc
type: command
executor: cmd
data: sc start $_SERVICE_NAME
output: null
created_at: '2023-04-06T03:56:28.095459+00:00'
updated_at: '2023-04-10T20:37:29.727924+00:00'
platforms:
  - Windows
tags:
  - persistence
  - service
verified: true
validated: true
---

# start-backdoor-service-sc

## Command

```cmd
sc start $_SERVICE_NAME
```

## Description

Starts a Windows service using the sc (Service Control) utility. Used to activate a backdoor service immediately after creation for instant persistence execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SERVICE_NAME | Name of the service to start (e.g., Backdoor) | Yes |

## Examples

### Basic Usage

```cmd
sc start Backdoor
```

## Expected Output

SERVICE_NAME: Backdoor
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 4  RUNNING
        ...

If already running: STATE: 4 RUNNING (no change).

## Related

- [[procedures/windows-elevated-services-backdoor-persistence]]
- [[commands/create-backdoor-service-powershell]]
