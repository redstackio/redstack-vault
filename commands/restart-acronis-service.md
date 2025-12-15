---
data: >-
  sc stop "Acronis Nonstop Backup Service" && sc start "Acronis Nonstop Backup
  Service"
tags:
  - service
  - execution
type: command
output: |-
  SERVICE_NAME: Acronis Nonstop Backup Service
  STATE: STOP_PENDING
  ...
  SERVICE_NAME: Acronis Nonstop Backup Service
  STATE: START_PENDING
executor: cmd
platforms:
  - Windows
id: 967c067c-1667-41aa-b99c-0eb36cf60f7e
created_at: '2025-12-14T17:26:17.531Z'
updated_at: '2025-12-14T17:26:17.531Z'
verified: false
validated: true
submitted: true
---
# restart-acronis-service

## Command

```cmd
sc stop "Acronis Nonstop Backup Service" && sc start "Acronis Nonstop Backup Service"
```

## Description

Stops and restarts the Acronis service to trigger hijacked path execution during startup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| stop | Stop flag | Yes |
| start | Start flag | Yes |
| "Acronis Nonstop Backup Service" | Service name | Yes |

## Examples

### Basic Usage

```cmd
sc stop "Acronis Nonstop Backup Service" && sc start "Acronis Nonstop Backup Service"
```

### Advanced Usage

```cmd
sc stop afcdpsrv && sc start afcdpsrv
```
(Short name)

## Expected Output

Service transitions from RUNNING to STOPPED then START_PENDING/RUNNING, with payload executing on start.

## Related

- [[procedures/Trigger-Service-Restart-to-Execute-Hijacked-Payload]]
