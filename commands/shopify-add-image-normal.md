---
id: 123e4567-e89b-12d3-a456-426614174005
name: shopify-add-image-normal
type: command
executor: bash
data: >-
  curl -X POST 'https://test-4925.myshopify.com/admin/products/922460995/images'
  -H 'Content-Type: application/x-www-form-urlencoded' -H 'X-CSRF-Token:
  F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' -d
  'utf8=%E2%9C%93&authenticity_token=F7cvLpquxqr%2BrFmnGVFhNEK6rV8njtebHikevxGlLJA%3D&product_id=922460995&image%5Bsrc%5D=https://example.com/image.jpg&_method=post'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.790Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - ssrf
  - shopify
verified: false
validated: true
submitted: true
---

# shopify-add-image-normal

## Command

```bash
curl -X POST 'https://test-4925.myshopify.com/admin/products/922460995/images' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -d 'utf8=%E2%9C%93&authenticity_token=F7cvLpquxqr%2BrFmnGVFhNEK6rV8njtebHikevxGlLJA%3D&product_id=922460995&image%5Bsrc%5D=https://example.com/image.jpg&_method=post'
```

## Description

Sends a legitimate POST request to add an image from a URL in Shopify admin, demonstrating the fetch behavior before SSRF exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H 'Content-Type: ...'` | Sets form data type | Yes |
| `-H 'X-CSRF-Token: ...'` | Anti-CSRF header | Yes |
| `-d '...'` | Form data with image[src] | Yes |
| `image[src]` | URL to fetch (valid image) | Yes |
| `product_id` | Target product ID | Yes |
| `authenticity_token` | CSRF token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://yourstore.myshopify.com/admin/products/123/images' -H 'Content-Type: application/x-www-form-urlencoded' -H 'X-CSRF-Token: TOKEN' -d 'image%5Bsrc%5D=https://example.com/img.jpg&product_id=123&_method=post'
```

### Advanced Usage

Include full headers and UTF-8 check for production.

## Expected Output

HTTP 200 OK with JSON like {"image":{"id":...,"src":...}}, image added to product.

## Related

- [[commands/shopify-ssrf-redirect]]
- [[procedures/Identify-Add-Image-from-URL-Endpoint]]
