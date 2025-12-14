---
data: sc qc "Acronis Nonstop Backup Service"
tags:
  - discovery
  - service
type: command
output: |-
  SERVICE_NAME: Acronis Nonstop Backup Service
          TYPE               : 10  WIN32_OWN_PROCESS
          STATE              : 4  RUNNING
                                  (STOPPABLE, NOT_PAUSABLE, ACCEPTS_SHUTDOWN)
          WIN32_EXIT_CODE    : 0  (0x0)
          SERVICE_EXIT_CODE  : 0  (0x0)
          CHECKPOINT         : 0x0
          WAIT_HINT          : 0x0
          BINARY_PATH_NAME   : C:\Program Files (x86)\Common Files\Acronis\CDP\afcdpsrv.exe
executor: cmd
platforms:
  - Windows
id: f6c24c71-ee1f-4234-b8dc-909b80907f0e
created_at: '2025-12-14T17:26:17.553Z'
updated_at: '2025-12-14T17:26:17.553Z'
verified: false
validated: true
submitted: true
---
# query-acronis-service-config

## Command

```cmd
sc qc "Acronis Nonstop Backup Service"
```

## Description

Queries the configuration of the Acronis Nonstop Backup Service to reveal the unquoted ImagePath, essential for identifying path hijacking vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| qc | Query configuration flag | Yes |
| "Acronis Nonstop Backup Service" | Exact service display name | Yes |

## Examples

### Basic Usage

```cmd
sc qc "Acronis Nonstop Backup Service"
```

### Advanced Usage

```cmd
sc qc afcdpsrv
```
(Using short name if known)

## Expected Output

Configuration details including BINARY_PATH_NAME without quotes, confirming vulnerability.

## Related

- [[procedures/Identify-Unquoted-Service-Path-in-Acronis-Service]]
