---
data: 'stunner recon tls://███████:443 -u ████████'
tags:
  - recon
  - turn
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.163Z'
id: dfb18769-0446-4a27-bdec-85da518a176c
verified: false
validated: true
submitted: true
---
---

# stunner-recon-turn-server

## Command

```bash
stunner recon tls://███████:443 -u ████████
```

## Description

Performs reconnaissance on a TURN server to identify if it's an open relay, peer IP restrictions, and protocol support using provided credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `tls://███████:443` | Target TURN server URL with TLS on port 443 | Yes |
| `-u ████████` | Username for TURN authentication | Yes |

## Examples

### Basic Usage

```bash
stunner recon tls://turn.example.com:443 -u tempuser
```

### Advanced Usage

```bash
stunner recon tls://turn.example.com:443 -u tempuser --verbose
```

## Expected Output

Reconnaissance results showing open relay status, allowed peer IPs (e.g., 127.0.0.1 permitted), and details like UDP/TCP relay support.

## Related

- [[Related Procedure: Reconnaissance-on-TURN-Server-Using-Stunner]]

---
