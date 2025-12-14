---
id: cmd-uuid-6
data: 'echo -e "HTTP/1.1 200 OK\n\nHello from netcat :)" | sudo nc -l 80'
tags:
  - listener
  - poc-capture
type: command
output: Waits for connection and sends response
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.655Z'
verified: false
validated: true
submitted: true
---
# nc-listen-port-80

## Command

```bash
echo -e "HTTP/1.1 200 OK\n\nHello from netcat :)" | sudo nc -l 80
```

## Description

Sets up a netcat listener on port 80 to capture and respond to SSRF requests during PoC testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l 80 | Listen on port 80 | Yes |

## Examples

### Basic Usage

```bash
echo -e "HTTP/1.1 200 OK\n\nHello from netcat :)" | sudo nc -l 80
```

## Expected Output

Waits for connection; upon SSRF hit, sends "Hello from netcat :)" and logs request.

## Related

- [[procedures/Bypass-SSRF-Filters-with-Hex-and-Decimal-IPs]]
- [[tools/nc]]
