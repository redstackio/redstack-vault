---
id: 7a24e357-bd09-4904-ad7f-972bc2b77b85
name: Start-a-Windows-Service
type: command
executor: command_prompt
data: sc.exe start $_SERVICE_NAME
output: |-
  C:\Windows\system32>sc.exe start pwnSVC

  SERVICE_NAME: pwnSVC
          TYPE               : 30  WIN32
          STATE              : 2  START_PENDING
                                  (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
          WIN32_EXIT_CODE    : 0  (0x0)
          SERVICE_EXIT_CODE  : 0  (0x0)
          CHECKPOINT         : 0x0
          WAIT_HINT          : 0x7d0
          PID                : 1884
          FLAGS              :
created_at: '2020-04-28T21:10:21.094874+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - execution
  - privilege-escalation
verified: true
validated: true
---

# Start-a-Windows-Service

## Command

```command_prompt
sc.exe start $_SERVICE_NAME
```

## Description

This command starts a registered Windows service, triggering its binary path execution (e.g., running a script as SYSTEM). Essential for activating persistence mechanisms or payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SERVICE_NAME | Name of the service to start (e.g., pwnSVC) | Yes |

## Examples

### Basic Usage

```command_prompt
sc.exe start pwnSVC
```

## Expected Output

```
C:\Windows\system32>sc.exe start pwnSVC

SERVICE_NAME: pwnSVC
        TYPE               : 30  WIN32
        STATE              : 2  START_PENDING
                                (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x7d0
        PID                : 1884
        FLAGS              :
```

Look for START_PENDING state and a PID; the payload executes regardless of subsequent errors.

## Related

- [[commands/Create-a-Windows-Service]]
- [[commands/Delete-a-Windows-Service]]
- [[procedures/Create-and-Run-Windows-Service-as-SYSTEM-Administrator]]
