---
data: >-
  curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' -H
  'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H
  'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' -H 'Cookie:
  COOKIES' -d 'src=SOME_URL'
tags:
  - ssrf
  - validation
type: command
output: HTTP/1.1 422 Unprocessable Entity
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.413Z'
id: d5b09892-22de-4cc7-8f73-5f72512886ce
verified: false
validated: true
submitted: true
---
# test-basic-url-validation

## Command

```bash
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -H 'Cookie: COOKIES' \
  -d 'src=SOME_URL'
```

## Description

Sends a POST request to Shopify's image insertion endpoint to test src parameter validation with arbitrary URLs, expecting rejection for invalid schemes/ports.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `src` | URL to test (e.g., http://example:8080) | Yes |
| X-CSRF-Token | Session token | Yes |
| Cookie | Auth cookies | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' -d 'src=http://example.com:8080/image.jpg' [headers]
```

### Advanced Usage

```bash
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' -d 'src=file:///etc/passwd' [headers]
```

## Expected Output

HTTP/1.1 422 Unprocessable Entity response body indicating invalid URL.

## Related

- [[commands/bypass-url-filters-with-redirection]]
