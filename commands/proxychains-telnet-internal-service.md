---
data: proxychains -f config telnet 127.0.0.1 5766
tags:
  - proxy
  - telnet
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.160Z'
id: 0a912298-47cd-4f5c-8723-1dca55a9e8ba
verified: false
validated: true
submitted: true
---
---

# proxychains-telnet-internal-service

## Command

```bash
proxychains -f config telnet 127.0.0.1 5766
```

## Description

Routes a telnet connection through a SOCKS proxy (from TURN relay) to access an internal service like coturn telnet on localhost port 5766.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f config` | Path to proxychains configuration file | Yes |
| `telnet 127.0.0.1 5766` | Telnet to target IP and port | Yes |

## Examples

### Basic Usage

```bash
proxychains -f /path/to/config telnet 127.0.0.1 5766
```

### Advanced Usage

```bash
proxychains -f config telnet 169.254.169.254 80
```

## Expected Output

Proxy chain logs followed by telnet connection notice and interactive prompt; e.g., "Escape character is '^]'" and coturn telnet interface.

## Related

- [[Related Procedure: Access-Internal-Services-via-TURN-SOCKS-Proxy]]

---
