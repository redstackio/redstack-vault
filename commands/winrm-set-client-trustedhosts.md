---
type: command
executor: powershell
data: 'winrm set winrm/config/client @{TrustedHosts="target-host, target-ip"}'
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - winrm
  - client
  - trusted
verified: true
validated: true
---

# winrm-set-client-trustedhosts

## Command

```powershell
winrm set winrm/config/client @{TrustedHosts="target-host, target-ip"}
```

## Description

Adds remote hosts to the WinRM client's trusted hosts list for non-domain authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @{TrustedHosts="list"} | Comma-separated hosts/IPs (use * for all) | Yes |

## Examples

### Basic Usage

```powershell
winrm set winrm/config/client @{TrustedHosts="192.168.1.100, winserver1"}
```

### Trust All

```powershell
winrm set winrm/config/client @{TrustedHosts="*"}
```

## Expected Output

TrustedHosts = target-host, target-ip

## Related

- [[procedures/windows-remoting-via-winrm]]
- [[commands/winrm-get-client-config]]
