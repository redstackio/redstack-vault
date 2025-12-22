---
type: command
executor: cmd
data: >-
  netsh advfirewall firewall add rule name="%_RULE_NAME%" dir=out action=allow
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

# netsh-advfirewall-add-outbound-rule

## Command

```cmd
netsh advfirewall firewall add rule name="%_RULE_NAME%" dir=out action=allow protocol=TCP localport=%_LOCALPORT%
```

## Description

Adds an outbound Windows Firewall rule to permit TCP traffic from a specific local port, enabling the pivot host to forward connections to internal destinations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `%_RULE_NAME%` | Descriptive name for the rule (e.g., "PortForwarding 4545") | Yes |
| `%_LOCALPORT%` | Local port to allow outbound (e.g., 4545) | Yes |

## Examples

### Basic Usage

```cmd
netsh advfirewall firewall add rule name="PortForwarding 4545" dir=out action=allow protocol=TCP localport=4545
```

### Advanced Usage

For HTTP forwarding:
```cmd
netsh advfirewall firewall add rule name="PortForwarding 80" dir=out action=allow protocol=TCP localport=80
```

## Expected Output

`Ok.` (rule added successfully).

## Related

- [[procedures/windows-netsh-port-forwarding]]
- [[commands/netsh-advfirewall-add-inbound-rule]]
