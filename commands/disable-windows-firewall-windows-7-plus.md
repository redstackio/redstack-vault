---
id: f42abda6-c23d-4648-84ec-b69a8d60da45
name: disable-windows-firewall-windows-7-plus
type: command
executor: command_prompt
data: netsh advfirewall set allprofiles state off
output: |-
  C:\>netsh advfirewall set allprofiles state off
  Ok.
created_at: '2019-11-15T01:22:12.204907+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - firewall-bypass
verified: true
validated: true
---

# disable-windows-firewall-windows-7-plus

## Command

```command_prompt
netsh advfirewall set allprofiles state off
```

## Description

Disables the Windows Advanced Firewall for all network profiles (domain, private, public) on Windows 7 and later.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| allprofiles | Applies to all firewall profiles | Yes |
| state off | Sets firewall state to disabled | Yes |

## Examples

### Basic Usage

```command_prompt
netsh advfirewall set allprofiles state off
```

### Advanced Usage

To re-enable: netsh advfirewall set allprofiles state on

## Expected Output

```
C:\>netsh advfirewall set allprofiles state off
Ok.
```

'Ok.' indicates successful disable; confirm with 'netsh advfirewall show allprofiles state' showing 'Off'.

## Related

- [[procedures/Disable-Windows-Firewall]]
- [[commands/allow-port-through-windows-firewall-windows-7-plus]]
