---
type: command
executor: powershell
data: 'winrm set winrm/config/service/auth @{Basic="true"}'
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - winrm
  - auth
verified: true
validated: true
---

# winrm-set-service-basic-auth

## Command

```powershell
winrm set winrm/config/service/auth @{Basic="true"}
```

## Description

Enables Basic authentication for the WinRM service, allowing plaintext username/password over HTTP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @{Basic="true"} | Hashtable to set Basic auth to true | Yes |

## Examples

### Basic Usage

```powershell
winrm set winrm/config/service/auth @{Basic="true"}
```

## Expected Output

Auth
    Basic = true

## Related

- [[procedures/windows-remoting-via-winrm]]
- [[commands/winrm-get-service-config]]
