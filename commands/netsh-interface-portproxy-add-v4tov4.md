---
type: command
executor: cmd
data: >-
  netsh interface portproxy add v4tov4 listenport=%_LISTENPORT%
  connectaddress=%_CONNECTADDRESS% connectport=%_CONNECTPORT%
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - port-forwarding
  - netsh
verified: true
validated: true
---

# netsh-interface-portproxy-add-v4tov4

## Command

```cmd
netsh interface portproxy add v4tov4 listenport=%_LISTENPORT% connectaddress=%_CONNECTADDRESS% connectport=%_CONNECTPORT%
```

## Description

Adds an IPv4 port forwarding rule using netsh, listening on the specified local port and forwarding TCP traffic to a destination IP and port. Useful for pivoting in Windows environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `%_LISTENPORT%` | Local port to listen on (e.g., 4545, 80) | Yes |
| `%_CONNECTADDRESS%` | Destination IP address to forward to (e.g., 192.168.50.44) | Yes |
| `%_CONNECTPORT%` | Destination port to forward to (e.g., 4545) | Yes |

## Examples

### Basic Usage

```cmd
netsh interface portproxy add v4tov4 listenport=4545 connectaddress=192.168.50.44 connectport=4545
```

### Advanced Usage

For RDP pivoting:
```cmd
netsh interface portproxy add v4tov4 listenport=3390 connectaddress=10.1.1.110 connectport=3389
```

## Expected Output

`Ok.` (indicating successful rule addition). If not elevated: `The requested operation requires elevation (Run as administrator).`

## Related

- [[procedures/windows-netsh-port-forwarding]]
- [[commands/netsh-advfirewall-add-inbound-rule]]
