---
id: c9ab23e4-05e1-419f-9c90-1879eac0e2c6
name: sc-stop-vulnerable-service
type: command
executor: cmd
data: sc stop upnphost
output: >-
  SERVICE_NAME: upnphost\n        TYPE               : 10 
  WIN32_OWN_PROCESS\n        STATE              : 1 
  STOPPED\n                                (STOPPABLE, NOT_PAUSABLE,
  IGNORES_RESET)\n        WIN32_EXIT_CODE    : 0  (0x0)\n       
  SERVICE_EXIT_CODE  : 0  (0x0)\n        CHECKPOINT         : 0x0\n       
  WAIT_HINT          : 0x0
created_at: '2023-04-06T03:56:29.545242+00:00'
updated_at: '2023-04-10T20:37:52.272360+00:00'
platforms:
  - Windows
tags:
  - service-management
verified: true
validated: true
---

# sc-stop-vulnerable-service

## Command

```cmd
sc stop upnphost
```

## Description

Stops a service to apply configuration changes, necessary before restarting for exploit execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sc stop | Stop service | Yes |
| upnphost | Service name | Yes |

## Examples

### Basic Usage

```cmd
sc stop upnphost
```

### Advanced Usage

```cmd
sc stop <service>
```

## Expected Output

```
SERVICE_NAME: upnphost
        STATE              : 1  STOPPED
```

Confirms service is stopped.

## Related

- [[procedures/Exploit-UPnP-Host-Service-for-Privilege-Escalation-on-Windows-XP-SP1]]
- [[commands/sc-start-vulnerable-service]]
