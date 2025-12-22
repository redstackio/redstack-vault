---
id: cmd-uuid-3
data: 'aws s3 cp phishing.html s3://dangling-bucket-name/ --acl public-read'
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
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.049Z'
verified: false
validated: true
submitted: true
---
# aws-upload-s3

## Command

```bash
aws s3 cp phishing.html s3://dangling-bucket-name/ --acl public-read
```

## Description

Uploads a file to an S3 bucket with public read access for hosting on a subdomain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `phishing.html` | Source file | Yes |
| `s3://dangling-bucket-name/` | Destination | Yes |
| `--acl public-read` | Set public access | No |

## Examples

### Basic Usage

```bash
aws s3 cp file.txt s3://bucket/
```

### Advanced Usage

```bash
aws s3 cp dir/ s3://bucket/ --recursive --acl public-read
```

## Expected Output

'upload: phishing.html to s3://dangling-bucket-name/phishing.html'.

## Related

- [[Related Procedure]]
