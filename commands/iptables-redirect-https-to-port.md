---
id: cmd-iptables-redirect-001
data: >-
  iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT
  --to-port 8080
tags:
  - nat
  - redirect
  - mitm
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:44.817Z'
verified: false
validated: true
submitted: true
---
# iptables-redirect-https-to-port

## Command

```bash
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080
```

## Description

This command redirects local incoming HTTPS traffic on port 443 from wlan0 to a local port (e.g., proxy listener), complementing DNAT for full transparent MITM in rogue AP scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t nat` | Specifies the NAT table | Yes |
| `-A PREROUTING` | Appends to PREROUTING chain | Yes |
| `-i wlan0` | Input interface (rogue WiFi) | Yes |
| `-p tcp` | Protocol match (TCP) | Yes |
| `--dport 443` | Destination port (HTTPS) | Yes |
| `-j REDIRECT` | Jump to REDIRECT target | Yes |
| `--to-port 8080` | Redirect to local port | Yes |

## Examples

### Basic Usage

```bash
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080
```

### Advanced Usage

```bash
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j REDIRECT --to-port 8080
```

## Expected Output

No output if successful; rule applied. Check with `iptables -t nat -L` for confirmation and traffic counters.

## Related

- [[commands/iptables-dnat-https-to-proxy]]
- [[procedures/Redirect-HTTPS-Traffic-Using-iptables]]
