---
data: >-
  tail -f /var/log/nginx/access.log | grep "GET /1.mp4 HTTP/1.1" | grep
  "Lavf/55.48.100"
tags:
  - ssrf
  - logging
type: command
output: >-
  Log entry: 127.0.0.1 - - [date] "GET /1.mp4 HTTP/1.1" 200 84 "-"
  "Lavf/55.48.100"
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.220Z'
id: 5c3000b7-d32e-4e0b-b413-d32982ef1a90
verified: false
validated: true
submitted: true
---
# server-get-external-mp4-1

## Command

```bash
tail -f /var/log/nginx/access.log | grep "GET /1.mp4 HTTP/1.1" | grep "Lavf/55.48.100"
```

## Description

Monitors Nginx logs for SSRF-induced GET request to /1.mp4 from Lavf. Use to confirm external fetch in SSRF attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/var/log/nginx/access.log` | Path to access log | Yes |

## Examples

### Basic Usage

```bash
tail -f /var/log/nginx/access.log | grep "GET /1.mp4"
```

### Advanced Usage

```bash
tail -f /var/log/nginx/access.log | grep "GET /1.mp4 HTTP/1.1" | grep "Lavf/55.48.100" | awk '{print $1, $9}'
```

## Expected Output

Log line showing successful GET with 200 status and file size.

## Related

- [[Related Procedure: Observe-SSRF-Requests]]
