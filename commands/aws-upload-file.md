---
id: cmd-uuid-004
name: aws-upload-file
type: command
executor: bash
data: 'aws s3 cp $1 s3://$2/$3'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.289Z'
platforms:
  - Linux
  - macOS
tags:
  - aws
  - upload
verified: false
validated: true
submitted: true
---

# aws-upload-file

## Command

```bash
aws s3 cp xss.html s3://shopify-assets/xss_unguessable3211231232.html
```

## Description

Uploads a local file to an S3 bucket using AWS CLI.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Local File | Path to file | Yes |
| Bucket | Target bucket | Yes |
| Key | Object key/path | Yes |

## Examples

### Basic Usage

```bash
aws s3 cp xss.html s3://shopify-assets/xss.html
```

### Advanced Usage

```bash
aws s3 cp xss.html s3://shopify-assets/path/xss.html --acl public-read
```

## Expected Output

upload: xss.html to s3://shopify-assets/xss_unguessable3211231232.html

## Related

- [[Related Procedure]]
