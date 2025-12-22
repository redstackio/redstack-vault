---
id: c136c221-68c1-4879-bc88-61f149c35d9e
name: enable-remoteadmin-firewall-service
type: command
executor: cmd
data: netsh firewall set service remoteadmin enable
output: null
created_at: '2023-04-06T03:56:31.036684+00:00'
updated_at: '2023-04-10T20:37:56.779209+00:00'
platforms:
  - Windows
tags:
  - firewall
  - rdp
verified: true
validated: true
---

# enable-remoteadmin-firewall-service

## Command

```cmd
netsh firewall set service remoteadmin enable
```

## Description

Enables the Remote Administration service in the Windows Firewall, allowing inbound connections for RDP-related admin access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| set service remoteadmin | Targets the remote admin service | Yes |
| enable | Activates the service rule | Yes |

## Examples

### Basic Usage

```cmd
netsh firewall set service remoteadmin enable
```

## Expected Output

```
Ok.
```

## Related

- [[procedures/windows-rdp-credential-usage]]
