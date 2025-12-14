---
id: cmd-uuid-7
data: nc -l -n -vv -p 443
tags:
  - capture
  - ssrf
type: command
output: 'Captured POST request with leaked form data to 127.0.0.1:443'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.714Z'
verified: false
validated: true
submitted: true
---
# netcat-listen-443

## Command

```bash
nc -l -n -vv -p 443
```

## Description

Listens for TCP connections on port 443 using netcat, capturing incoming SSRF requests without DNS resolution and with verbose logging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | Listen mode | Yes |
| -n | No DNS | Yes |
| -vv | Very verbose | Yes |
| -p 443 | Port 443 | Yes |

## Examples

### Basic Usage

```bash
nc -l -n -vv -p 443
```

### Advanced Usage

For port 80: nc -l -n -vv -p 80

## Expected Output

Verbose connection logs and full HTTP request capture.

## Related

- [[commands/request-token-with-leak]]
