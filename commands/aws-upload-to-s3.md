---
data: 'aws s3 cp $1 s3://$2/'
tags:
  - aws
  - upload
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 51111e4e-5146-473d-a106-47d52cc39909
created_at: '2025-12-14T04:38:49.433Z'
updated_at: '2025-12-14T04:38:49.433Z'
verified: false
validated: true
submitted: true
---
# aws-upload-to-s3

## Command

```bash
aws s3 cp index.html s3://subdomain.mozaws.net/
```

## Description

Uploads files to an S3 bucket, allowing deployment of content on a taken-over subdomain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `index.html` | Local file to upload | Yes |
| `s3://subdomain.mozaws.net/` | Target bucket | Yes |

## Examples

### Basic Usage

```bash
aws s3 cp demo.html s3://bucket/
```

### Advanced Usage

```bash
aws s3 cp demo.html s3://bucket/ --acl public-read
```

## Expected Output

"upload: demo.html to s3://bucket/demo.html".

## Related

- [[Related Procedure]]
