---
id: cc5ef69e-47da-4770-a771-3d9a695a724f
name: sc-start-vulnerable-service
type: command
executor: cmd
data: sc start upnphost
output: >-
  SERVICE_NAME: upnphost\n        TYPE               : 10 
  WIN32_OWN_PROCESS\n        STATE              : 4 
  RUNNING\n                                (STOPPABLE, NOT_PAUSABLE,
  ACCEPTS_SHUTDOWN)\n        WIN32_EXIT_CODE    : 0  (0x0)\n       
  SERVICE_EXIT_CODE  : 0  (0x0)\n        CHECKPOINT         : 0x0\n       
  WAIT_HINT          : 0x0x7d0
created_at: '2023-04-06T03:56:29.545334+00:00'
updated_at: '2023-04-10T20:37:52.272360+00:00'
platforms:
  - Windows
tags:
  - service-management
verified: true
validated: true
---

# sc-start-vulnerable-service

## Command

```cmd
sc start upnphost
```

## Description

Starts the service, triggering the modified binary path to execute the payload as SYSTEM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sc start | Start service | Yes |
| upnphost | Service name | Yes |

## Examples

### Basic Usage

```cmd
sc start upnphost
```

### Advanced Usage

```cmd
sc start <service>
```

## Expected Output

```
SERVICE_NAME: upnphost
        STATE              : 4  RUNNING
```

Service running; check for payload effects (e.g., new user or shell).

## Related

- [[procedures/Exploit-UPnP-Host-Service-for-Privilege-Escalation-on-Windows-XP-SP1]]
- [[commands/sc-stop-vulnerable-service]]
