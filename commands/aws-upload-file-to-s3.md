---
id: 123e4567-e89b-12d3-a456-426614174007
name: aws-upload-file-to-s3
type: command
executor: bash
data: 'aws s3 cp XSS.html s3://users.tweetdeck.com/XSS.html --region us-east-1'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.490Z'
platforms:
  - Linux
  - macOS
tags:
  - aws
  - s3
  - upload
verified: false
validated: true
submitted: true
---

# aws-upload-file-to-s3

## Command

```bash
aws s3 cp XSS.html s3://users.tweetdeck.com/XSS.html --region us-east-1
```

## Description

Uploads a file to S3 to host content on the subdomain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cp` | Copy file | Yes |
| `XSS.html` | Local file | Yes |
| `s3://...` | Destination | Yes |
| `--region` | AWS region | Yes |

## Examples

### Basic Usage

```bash
aws s3 cp file.html s3://bucket/file.html
```

## Expected Output

"upload: file.html to s3://bucket/file.html"

## Related

- [[Related Procedure]]
