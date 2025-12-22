---
id: 2553c253-0588-4190-a9f2-56c4547f0a85
name: accesschk-check-authenticated-users-service-permissions
type: command
executor: cmd
data: accesschk.exe -uwcqv "Authenticated Users" * /accepteula
output: >-
  RW SSDPSRV\n        SERVICE_ALL_ACCESS\nRW upnphost\n       
  SERVICE_ALL_ACCESS
created_at: '2023-04-06T03:56:29.544808+00:00'
updated_at: '2023-04-10T20:37:52.272360+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - service-enumeration
verified: true
validated: true
---

# accesschk-check-authenticated-users-service-permissions

## Command

```cmd
accesschk.exe -uwcqv "Authenticated Users" * /accepteula
```

## Description

This command uses AccessChk to enumerate Windows services where the Authenticated Users group has write, control, or query permissions, identifying potential privilege escalation vectors like misconfigured services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Show user/group accounts | Yes |
| -w | Check for write access | Yes |
| -c | Check for control access | Yes |
| -q | Quiet mode (no headers) | Yes |
| -v | Verbose output | Yes |
| "Authenticated Users" | Target SID/group | Yes |
| * | All services | Yes |
| /accepteula | Auto-accept EULA | Yes |

## Examples

### Basic Usage

```cmd
accesschk.exe -uwcqv "Authenticated Users" * /accepteula
```

### Advanced Usage

```cmd
accesschk.exe -uwcqv "Authenticated Users" upnphost /accepteula
```

## Expected Output

```
RW SSDPSRV
        SERVICE_ALL_ACCESS
RW upnphost
        SERVICE_ALL_ACCESS
```

Services with RW and SERVICE_ALL_ACCESS indicate vulnerability to modification by low-priv users.

## Related

- [[procedures/Exploit-UPnP-Host-Service-for-Privilege-Escalation-on-Windows-XP-SP1]]
- [[commands/accesschk-check-upnphost-service-permissions]]
