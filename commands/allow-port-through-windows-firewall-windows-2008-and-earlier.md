---
id: 00d49676-35d6-40e4-b979-5ea20a0c500e
name: allow-port-through-windows-firewall-windows-2008-and-earlier
type: command
executor: command_prompt
data: netsh firewall add portopening TCP $_PORT "Open Port $_PORT"
output: 'C:\netsh firewall add portopening 80 "Open Port 80"'
created_at: '2019-11-15T01:22:12.239504+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - firewall-bypass
verified: true
validated: true
---

# allow-port-through-windows-firewall-windows-2008-and-earlier

## Command

```command_prompt
netsh firewall add portopening TCP $_PORT "Open Port $_PORT"
```

## Description

This legacy command opens a TCP port for inbound connections on Windows Server 2008 and earlier systems using the basic firewall interface.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | Port number to open (e.g., 80) | Yes |
| TCP | Protocol type | Yes |
| "Open Port $_PORT" | Descriptive name for the rule | Yes |

## Examples

### Basic Usage

```command_prompt
netsh firewall add portopening TCP 80 "Open Port 80"
```

### Advanced Usage

For a custom port:

```command_prompt
netsh firewall add portopening TCP 4444 "Open Port 4444"
```

## Expected Output

```
C:\netsh firewall add portopening 80 "Open Port 80"
```

The command executes without verbose output on success; check with 'netsh firewall show portopening'.

## Related

- [[procedures/Disable-Windows-Firewall]]
- [[commands/disable-windows-firewall-windows-2008-and-earlier]]
