---
id: c136c221-68c1-4879-bc88-61f149c35d9f
name: enable-remotedesktop-firewall-service
type: command
executor: cmd
data: netsh firewall set service remotedesktop enable
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

# enable-remotedesktop-firewall-service

## Command

```cmd
netsh firewall set service remotedesktop enable
```

## Description

Enables the Remote Desktop service in the Windows Firewall, permitting RDP traffic on port 3389.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| set service remotedesktop | Targets the RDP service | Yes |
| enable | Activates the service rule | Yes |

## Examples

### Basic Usage

```cmd
netsh firewall set service remotedesktop enable
```

## Expected Output

```
Ok.
```

## Related

- [[procedures/windows-rdp-credential-usage]]
