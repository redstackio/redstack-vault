---
data: >-
  tail -f /var/log/nginx/access.log | grep "GET /2.mp4 HTTP/1.1" | grep
  "Lavf/55.48.100"
tags:
  - ssrf
  - logging
type: command
output: >-
  Log entry: 127.0.0.1 - - [date] "GET /2.mp4 HTTP/1.1" 404 169 "-"
  "Lavf/55.48.100"
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.215Z'
id: 4e86b9f2-23a6-4eda-a8c6-1652ef2cc9c8
verified: false
validated: true
submitted: true
---
# server-get-external-mp4-2

## Command

```bash
tail -f /var/log/nginx/access.log | grep "GET /2.mp4 HTTP/1.1" | grep "Lavf/55.48.100"
```

## Description

Monitors logs for SSRF request to non-existent /2.mp4, confirming arbitrary URL capability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/var/log/nginx/access.log` | Log file path | Yes |

## Examples

### Basic Usage

```bash
tail -f access.log | grep "/2.mp4"
```

### Advanced Usage

```bash
tail -f /var/log/nginx/access.log | grep "GET /2.mp4" | grep Lavf
```

## Expected Output

Log showing 404 response, indicating failed but arbitrary fetch.

## Related

- [[Related Procedure: Observe-SSRF-Requests]]
