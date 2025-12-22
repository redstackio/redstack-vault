---
id: 3c6f2451-5c62-461a-8d9a-c567106c35d1
name: allow-application-through-windows-firewall-windows-7-plus
type: command
executor: command_prompt
data: >-
  netsh advfirewall firewall add rule name="Allow $_PROGRAM to bypass firewall
  rules" dir=in action=allow program="C:\$_PATH\$_PROGRAM.exe" enable=yes
output: >-
  C:\Windows\System32>netsh advfirewall firewall add rule name="Allow calc.exe
  to bypass firewall rules" dir=in action=allow
  program="C:\Windows\System32\calc.exe" enable=yes

  Ok.
created_at: '2019-11-15T01:22:12.216549+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - firewall-bypass
verified: true
validated: true
---

# allow-application-through-windows-firewall-windows-7-plus

## Command

```command_prompt
netsh advfirewall firewall add rule name="Allow $_PROGRAM to bypass firewall rules" dir=in action=allow program="C:\$_PATH\$_PROGRAM.exe" enable=yes
```

## Description

This command creates an inbound firewall rule allowing a specific application to receive network connections on Windows 7 and later, bypassing default blocks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PROGRAM | Name of the application (e.g., calc.exe) | Yes |
| $_PATH | Directory path to the executable (e.g., Windows\System32) | Yes |
| name | Rule name for identification | Yes |
| dir=in | Direction: inbound traffic | Yes |
| action=allow | Permit the connection | Yes |
| enable=yes | Immediately enable the rule | Yes |

## Examples

### Basic Usage

```command_prompt
netsh advfirewall firewall add rule name="Allow calc.exe to bypass firewall rules" dir=in action=allow program="C:\Windows\System32\calc.exe" enable=yes
```

### Advanced Usage

For a custom tool in a different path:

```command_prompt
netsh advfirewall firewall add rule name="Allow MyTool to bypass firewall rules" dir=in action=allow program="C:\Tools\MyTool.exe" enable=yes
```

## Expected Output

```
C:\Windows\System32>netsh advfirewall firewall add rule name="Allow calc.exe to bypass firewall rules" dir=in action=allow program="C:\Windows\System32\calc.exe" enable=yes
Ok.
```

Success returns 'Ok.'; errors indicate insufficient privileges or invalid paths.

## Related

- [[procedures/Disable-Windows-Firewall]]
- [[commands/allow-port-through-windows-firewall-windows-7-plus]]
