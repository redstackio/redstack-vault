---
type: command
executor: powershell
data: winrm get winrm/config/service
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - winrm
  - config
verified: true
validated: true
---

# winrm-get-service-config

## Command

```powershell
winrm get winrm/config/service
```

## Description

Retrieves the WinRM service configuration, including authentication methods and security settings like AllowUnencrypted.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Gets full service config | No |

## Examples

### Basic Usage

```powershell
winrm get winrm/config/service
```

## Expected Output

Config
    MaxConcurrentOperations = 4294967295
    MaxConcurrentOperationsPerUser = 1500
    ...
    Auth
        Basic = false
        ...
    AllowUnencrypted = false

## Related

- [[procedures/windows-remoting-via-winrm]]
- [[commands/winrm-set-service-basic-auth]]
