---
id: cmd-netstat-count-001
data: netstat -nt | grep ESTABLISHED | grep -c ████32
tags:
  - network
  - monitoring
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.923Z'
verified: false
validated: true
submitted: true
---
# netstat-connection-count

## Command

```bash
netstat -nt | grep ESTABLISHED | grep -c ████32
```

## Description

Counts ESTABLISHED TCP connections to a specific IP (proxy) to confirm pending DoS requests from the attacker server side.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-nt` | Numeric TCP, no hostname resolution | Yes |
| `grep ESTABLISHED` | Filter for established connections | Yes |
| `grep -c IP` | Count lines matching IP | Yes |

## Examples

### Basic Usage

```bash
netstat -nt | grep ESTABLISHED | grep -c 1.2.3.4
```

### Advanced Usage

netstat -ntu for UDP too

## Expected Output

20 (or number of connections)

## Related

- [[procedures/Verify-and-Monitor-DoS-Impact]]
- [[tools/netstat]]
