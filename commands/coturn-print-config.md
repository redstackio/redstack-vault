---
data: '> pc'
tags:
  - coturn
  - config
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.157Z'
id: 5b31917d-cad8-4790-940e-2f21e3b9c4b0
verified: false
validated: true
submitted: true
---
---

# coturn-print-config

## Command

```bash
> pc
```

## Description

In an interactive coturn telnet session, prints the current server configuration for reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pc` | Print config command | Yes |

## Examples

### Basic Usage

Within telnet: `> pc`

## Expected Output

Detailed config dump including verbose mode, listener addresses (e.g., 0.0.0.0:443), relay ports (49152-65535), DB path (e.g., /var/lib/coturn/turnserver.db), realm, and more.

## Related

- [[Related Procedure: Access-Internal-Services-via-TURN-SOCKS-Proxy]]

---
