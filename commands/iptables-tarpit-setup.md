---
data: iptables -t mangle -A PREROUTING -p tcp --dport 12345 -j TARPIT
tags:
  - dos
  - tarpit
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:08.965Z'
id: adced068-30c4-4b34-a63a-7e5b33051e06
verified: false
validated: true
submitted: true
---
# iptables-tarpit-setup

## Command

```bash
iptables -t mangle -A PREROUTING -p tcp --dport 12345 -j TARPIT
```

## Description

Set up TARPIT to hold TCP connections on port 12345 for DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t mangle` | Table for mangling | Yes |
| `-A PREROUTING` | Chain to append | Yes |
| `--dport 12345` | Destination port | Yes |
| `-j TARPIT` | Jump to TARPIT target | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

No output; rule added (check with `iptables -t mangle -L`).

## Related

- [[procedures/Explore-FTP-DoS-with-Iptables-Tarpit]]
