---
data: 'aws s3 cp $1 s3://$2/ --acl public-read'
tags:
  - aws
  - s3
  - upload
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: e7b3a0c7-6912-4ea6-adeb-b03c9399ac49
created_at: '2025-12-14T04:38:49.832Z'
updated_at: '2025-12-14T04:38:49.832Z'
verified: false
validated: true
submitted: true
---
# aws-s3-cp-upload-poc

## Command

```bash
aws s3 cp $1 s3://$2/ --acl public-read
```

## Description

Uploads a file to an S3 bucket, making it public for serving via CloudFront in takeover demos.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $1 | Local file (e.g., index.html) | Yes |
| $2 | Bucket name | Yes |

## Examples

### Basic Usage

```bash
aws s3 cp index.html s3://attacker-bucket/
```

### Advanced Usage

```bash
aws s3 cp index.html s3://bucket/ --acl public-read --content-type text/html
```

## Expected Output

upload: index.html to s3://bucket/index.html

## Related

- [[Related Procedure]]
