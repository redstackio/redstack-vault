---
id: 1c5bf85b-996e-479b-afcd-562f42086dc0
name: ping-evil-website
type: command
executor: bash
data: ping -c 4 $_MALICIOUS_HOST
output: null
created_at: '2023-04-06T03:56:31.693380+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - recon
verified: true
validated: true
---

# ping-evil-website

## Command

```bash
ping -c 4 $_MALICIOUS_HOST
```

## Description

Pings the malicious website to confirm network reachability from the testing environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -c 4 | Number of pings | No |
| $_MALICIOUS_HOST | Target host | Yes |

## Examples

### Basic Usage

```bash
ping -c 4 evil-website.tld
```

## Expected Output

64 bytes from 192.168.1.100: icmp_seq=1 ttl=64 time=1.2 ms

## Related

- [[procedures/Open-URL-Redirection-Exploitation]]
- [[commands/get-ip-address]]
