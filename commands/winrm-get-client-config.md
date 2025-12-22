---
type: command
executor: powershell
data: winrm get winrm/config/client
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - winrm
  - client
verified: true
validated: true
---

# winrm-get-client-config

## Command

```powershell
winrm get winrm/config/client
```

## Description

Displays the WinRM client configuration, such as trusted hosts and encryption settings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Gets full client config | No |

## Examples

### Basic Usage

```powershell
winrm get winrm/config/client
```

## Expected Output

Config
    MaxEnvelopeSizekb = 500
    ...
    Auth
        Basic = true
    TrustedHosts = *
    AllowUnencrypted = false

## Related

- [[procedures/windows-remoting-via-winrm]]
- [[commands/winrm-set-client-allow-unencrypted]]
