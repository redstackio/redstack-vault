---
id: cmd-ping-resolve-927413
data: ping -c 4 zomato.com
tags:
  - recon
type: command
output: |-
  PING zomato.com (52.77.124.190) 56(84) bytes of data.
  64 bytes from 52.77.124.190: icmp_seq=1 ttl=... time=... ms
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.635Z'
verified: false
validated: true
submitted: true
---
# ping-resolve-ip

## Command

```bash
ping -c 4 zomato.com
```

## Description

Resolves a domain to its IP address using ICMP echo requests, confirming reachability. Used in initial recon to target Zomato's infrastructure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c 4` | Limit to 4 pings | No |
| `zomato.com` | Target domain | Yes |

## Examples

### Basic Usage

```bash
ping zomato.com
```

### Advanced Usage

```bash
ping -c 10 -i 1 zomato.com
```

## Expected Output

Displays resolved IP (52.77.124.190) and response times, indicating live host.

## Related

- [[Related Procedure: IP-Address-Discovery-via-Ping]]
