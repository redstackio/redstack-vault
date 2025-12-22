---
id: 421f09bc-ff32-4613-8e62-9611d00c7091
name: accesschk-check-upnphost-service-permissions
type: command
executor: cmd
data: accesschk.exe -ucqv upnphost
output: >-
  upnphost\n  RW NT AUTHORITY\\SYSTEM\n        SERVICE_ALL_ACCESS\n  RW
  BUILTIN\\Administrators\n        SERVICE_ALL_ACCESS\n  RW NT
  AUTHORITY\\Authenticated Users\n        SERVICE_ALL_ACCESS\n  RW
  BUILTIN\\Power Users\n        SERVICE_ALL_ACCESS
created_at: '2023-04-06T03:56:29.544864+00:00'
updated_at: '2023-04-10T20:37:52.272360+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - service-enumeration
verified: true
validated: true
---

# accesschk-check-upnphost-service-permissions

## Command

```cmd
accesschk.exe -ucqv upnphost
```

## Description

This command inspects permissions on the UPnP Host service to confirm if low-privileged groups like Authenticated Users can modify it for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Show user accounts | Yes |
| -c | Check control access | Yes |
| -q | Quiet mode | Yes |
| -v | Verbose output | Yes |
| upnphost | Target service name | Yes |

## Examples

### Basic Usage

```cmd
accesschk.exe -ucqv upnphost
```

### Advanced Usage

```cmd
accesschk.exe -ucqv "NT AUTHORITY\\Authenticated Users" upnphost
```

## Expected Output

```
upnphost
  RW NT AUTHORITY\SYSTEM
        SERVICE_ALL_ACCESS
  RW BUILTIN\Administrators
        SERVICE_ALL_ACCESS
  RW NT AUTHORITY\Authenticated Users
        SERVICE_ALL_ACCESS
  RW BUILTIN\Power Users
        SERVICE_ALL_ACCESS
```

RW for Authenticated Users confirms exploitability.

## Related

- [[procedures/Exploit-UPnP-Host-Service-for-Privilege-Escalation-on-Windows-XP-SP1]]
- [[commands/accesschk-check-authenticated-users-service-permissions]]
