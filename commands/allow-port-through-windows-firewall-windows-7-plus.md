---
id: b8ffb019-da27-48ed-b8de-0a64e01323ae
name: allow-port-through-windows-firewall-windows-7-plus
type: command
executor: command_prompt
data: >-
  netsh advfirewall firewall add rule name="Open Port $_PORT" dir=in
  action=allow protocol=TCP localport=$_PORT
output: >-
  C:\>netsh advfirewall firewall add rule name="Open Port 80" dir=in
  action=allow protocol=TCP localport=80

  Ok.
created_at: '2019-11-15T01:22:12.204754+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - firewall-bypass
verified: true
validated: true
---

# allow-port-through-windows-firewall-windows-7-plus

## Command

```command_prompt
netsh advfirewall firewall add rule name="Open Port $_PORT" dir=in action=allow protocol=TCP localport=$_PORT
```

## Description

Creates an inbound TCP rule to allow traffic on a specific port for Windows 7 and later, enabling remote access without full firewall disable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | Local port number (e.g., 80) | Yes |
| name="Open Port $_PORT" | Rule name | Yes |
| dir=in | Inbound direction | Yes |
| action=allow | Allow the traffic | Yes |
| protocol=TCP | TCP protocol | Yes |
| localport=$_PORT | Port to open | Yes |

## Examples

### Basic Usage

```command_prompt
netsh advfirewall firewall add rule name="Open Port 80" dir=in action=allow protocol=TCP localport=80
```

### Advanced Usage

For multiple ports, run sequentially or use a script.

## Expected Output

```
C:\>netsh advfirewall firewall add rule name="Open Port 80" dir=in action=allow protocol=TCP localport=80
Ok.
```

'Ok.' confirms rule creation; verify with 'netsh advfirewall firewall show rule name="Open Port 80"'.

## Related

- [[procedures/Disable-Windows-Firewall]]
- [[commands/allow-application-through-windows-firewall-windows-7-plus]]
