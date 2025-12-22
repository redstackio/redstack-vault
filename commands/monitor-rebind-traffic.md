---
data: tcpdump -i any port 80 -w ssrf_capture.pcap
tags:
  - monitor
  - traffic
  - tcpdump
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.625Z'
id: 0bdc6c24-c0a1-430e-b6d3-94a023a7952b
verified: false
validated: true
submitted: true
---
# monitor-rebind-traffic

## Command

```bash
tcpdump -i any port 80 -w ssrf_capture.pcap
```

## Description

This command uses tcpdump to capture network traffic on port 80, monitoring for SSRF requests during DNS rebinding exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i any` | Interface to capture on | Yes |
| `port 80` | Filter for HTTP traffic | Yes |
| `-w` | Output file for capture | Yes |

## Examples

### Basic Usage

```bash
tcpdump -i any port 80 -w capture.pcap
```

### Advanced Usage

```bash
tcpdump -i any port 80 -w capture.pcap -s 0 -w -
```

## Expected Output

Binary pcap file with captured packets; use Wireshark to view SSRF requests to internal IPs.

## Related

- [[Related Procedure|procedures/Exploit-DNS-Rebinding-for-SSRF-in-Nextcloud]]
