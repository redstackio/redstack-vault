---
data: 'curl -I https://target-domain/page'
tags:
  - web
  - headers
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: ad6cbb75-4c08-4e71-8e01-eedacbad8f92
created_at: '2025-12-14T03:15:26.520Z'
updated_at: '2025-12-14T03:15:26.520Z'
verified: false
validated: true
submitted: true
---
# curl-check-expires

## Command

```bash
curl -I https://target-domain/page
```

## Description

Fetches HTTP headers from a URL to inspect cache-related info like 'Expires' for timing attacks involving cached content poisoning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -I | Head request only | Yes |
| URL | Target page | Yes |

## Examples

### Basic Usage

```bash
curl -I https://example.com/
```

### Advanced Usage

```bash
curl -I -H "User-Agent: Mozilla/5.0" https://site.com/page
```

## Expected Output

Headers like 'Expires: Wed, 01 Oct 2023 12:00:00 GMT' or 'Cache-Control: max-age=300'.

## Related

- [[procedures/Wait-for-Cache-Expiration-and-Serve-to-Victims]]
