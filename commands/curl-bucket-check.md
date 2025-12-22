---
id: cmd-uuid-002
name: curl-bucket-check
type: command
executor: bash
data: 'curl https://$1.s3.amazonaws.com'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.299Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - recon
verified: false
validated: true
submitted: true
---

# curl-bucket-check

## Command

```bash
curl https://shopify-assets.s3.amazonaws.com
```

## Description

Checks S3 bucket existence by attempting anonymous GET on the root, revealing if unregistered.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Bucket Name | S3 bucket to probe | Yes |

## Examples

### Basic Usage

```bash
curl https://shopify-assets.s3.amazonaws.com
```

### Advanced Usage

```bash
curl -I https://shopify-assets.s3.amazonaws.com
```

## Expected Output

XML error: <Error><Code>NoSuchBucket</Code>...</Error>

## Related

- [[Related Procedure]]
