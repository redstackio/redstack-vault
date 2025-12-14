---
id: cmd-uuid-aws-s3-upload
data: 'aws s3 cp FILE s3://BUCKET_NAME/'
tags:
  - aws
  - cloud
  - upload
type: command
output: 'upload: FILE to s3://BUCKET_NAME/FILE'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.457Z'
verified: false
validated: true
submitted: true
---
# aws-s3-upload

## Command

```bash
aws s3 cp FILE s3://BUCKET_NAME/
```

## Description

Uploads files to an AWS S3 bucket, essential for hosting content on claimed subdomains.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cp` | Copy operation | Yes |
| `FILE` | Local file path | Yes |
| `s3://BUCKET_NAME/` | Destination bucket | Yes |

## Examples

### Basic Usage

```bash
aws s3 cp index.html s3://dangling-bucket/
```

### Advanced Usage

```bash
aws s3 cp --recursive ./site/ s3://dangling-bucket/
```

## Expected Output

Confirmation of upload, e.g., "upload: index.html to s3://dangling-bucket/index.html".

## Related

- [[procedures/Host-Arbitrary-Content-on-Taken-Over-Subdomain]]
