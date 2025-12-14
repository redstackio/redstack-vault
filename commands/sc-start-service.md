---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: sc start "UniFi Video"
tags:
  - service
  - trigger
type: command
output: |-
  SERVICE_NAME: UniFi Video
          TYPE               : 10  WIN32_OWN_PROCESS
          STATE              : 4  RUNNING
          ...
          PID                 : 1234
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:44.476Z'
verified: false
validated: true
submitted: true
---
# sc-start-service

## Command

```cmd
sc start "UniFi Video"
```

## Description

Starts the UniFi Video service, triggering execution of modified files in the installation directory to activate an escalation payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Service Name | Name of the target service (e.g., UniFi Video) | Yes |

## Examples

### Basic Usage

```cmd
sc start "UniFi Video"
```

### Advanced Usage

```cmd
sc start "UniFi Video" type= own
```

## Expected Output

SERVICE_NAME: UniFi Video
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 4  RUNNING

Service starts without errors, loading modified components.

## Related

- [[Related Procedure|procedures/Exploit-Weak-ACLs-in-UniFi-Video-Directory]]
