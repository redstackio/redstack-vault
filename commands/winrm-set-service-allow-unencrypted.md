---
type: command
executor: powershell
data: 'winrm set winrm/config/service @{AllowUnencrypted="true"}'
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - winrm
  - security
verified: true
validated: true
---

# winrm-set-service-allow-unencrypted

## Command

```powershell
winrm set winrm/config/service @{AllowUnencrypted="true"}
```

## Description

Allows unencrypted (HTTP) traffic to the WinRM service; use only in isolated labs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @{AllowUnencrypted="true"} | Hashtable to enable unencrypted | Yes |

## Examples

### Basic Usage

```powershell
winrm set winrm/config/service @{AllowUnencrypted="true"}
```

## Expected Output

AllowUnencrypted = true

## Related

- [[procedures/windows-remoting-via-winrm]]
- [[commands/winrm-get-service-config]]
