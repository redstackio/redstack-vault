---
type: command
executor: cmd
data: >-
  netsh advfirewall firewall add rule name="%_RULE_NAME%" dir=in action=allow
  protocol=TCP localport=%_LOCALPORT%
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - firewall
  - netsh
verified: true
validated: true
---

# netsh-advfirewall-add-inbound-rule

## Command

```cmd
netsh advfirewall firewall add rule name="%_RULE_NAME%" dir=in action=allow protocol=TCP localport=%_LOCALPORT%
```

## Description

Adds an inbound Windows Firewall rule to allow TCP traffic on a specific local port, necessary for port forwarding setups to receive incoming connections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `%_RULE_NAME%` | Descriptive name for the rule (e.g., "PortForwarding 80") | Yes |
| `%_LOCALPORT%` | Local port to allow (e.g., 80, 4545) | Yes |

## Examples

### Basic Usage

```cmd
netsh advfirewall firewall add rule name="PortForwarding 80" dir=in action=allow protocol=TCP localport=80
```

### Advanced Usage

For multiple ports, run separately:
```cmd
netsh advfirewall firewall add rule name="PortForwarding 4545" dir=in action=allow protocol=TCP localport=4545
```

## Expected Output

`Ok.` (rule added successfully).

## Related

- [[procedures/windows-netsh-port-forwarding]]
- [[commands/netsh-advfirewall-add-outbound-rule]]
