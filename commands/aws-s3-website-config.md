---
id: cmd-aws-website
type: command
executor: bash
data: >-
  aws s3 website s3://$BUCKET --index-document index.html --error-document
  error.html
output: Website configuration applied
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.641Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - s3
  - hosting
verified: false
validated: true
submitted: true
---

# aws-s3-website-config

## Command

```bash
aws s3 website s3://$BUCKET --index-document index.html --error-document error.html
```

## Description

Configures an S3 bucket for static website hosting, enabling subdomain content serving.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://$BUCKET` | Target bucket | Yes |
| `--index-document` | Default file | Yes |
| `--error-document` | Error page | Yes |

## Examples

### Basic Usage

```bash
aws s3 website s3://happymondays.starbucks.com --index-document index.html
```

## Expected Output

Configuration success message.

## Related

- [[Related Procedure: Claim Subdomain by Creating AWS S3 Bucket]]
