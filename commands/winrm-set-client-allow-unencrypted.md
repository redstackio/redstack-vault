---
type: command
executor: powershell
data: 'winrm set winrm/config/client @{AllowUnencrypted="true"}'
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - winrm
  - client
  - security
verified: true
validated: true
---

# winrm-set-client-allow-unencrypted

## Command

```powershell
winrm set winrm/config/client @{AllowUnencrypted="true"}
```

## Description

Enables the WinRM client to send unencrypted traffic to remote services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @{AllowUnencrypted="true"} | Hashtable to enable unencrypted | Yes |

## Examples

### Basic Usage

```powershell
winrm set winrm/config/client @{AllowUnencrypted="true"}
```

## Expected Output

AllowUnencrypted = true

## Related

- [[procedures/windows-remoting-via-winrm]]
- [[commands/winrm-get-client-config]]
