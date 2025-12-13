---
data: tcpdump -i any port 53
tags:
  - monitoring
  - dns
type: command
executor: bash
platforms:
  - Linux
id: f4f0fb86-df7a-434d-a40e-da1e0a34340c
created_at: '2025-12-13T09:00:27.623Z'
updated_at: '2025-12-13T09:00:27.623Z'
verified: false
validated: true
submitted: true
---
# Monitor DNS Requests

## Command

```bash
tcpdump -i any port 53
```

## Description

This command captures network traffic on port 53 to monitor DNS requests for exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i any` | Interface to listen on | Yes |
| `port 53` | Filter for DNS port | Yes |

## Examples

### Basic Usage

```bash
tcpdump -i any port 53
```

### Advanced Usage

```bash
tcpdump -i any port 53 -w capture.pcap
```

## Expected Output

Live capture of DNS packets, showing queries from the target.

## Related

- [[procedures/Monitor-DNS-for-Data-Exfiltration]]
