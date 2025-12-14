---
data: 'aws s3 rb s3://s3-r-w'
tags:
  - aws
  - s3
  - delete
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.029Z'
id: 8cfa2451-8c3a-4b18-8f80-a37161aaa962
verified: false
validated: true
submitted: true
---
---

# aws-s3-rb-delete

## Command

```bash
aws s3 rb s3://s3-r-w
```

## Description

Recursively deletes the S3 bucket and all its contents, enabling takeover if public delete is allowed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| s3://s3-r-w | Target S3 bucket URI | Yes |
| --force | Recursively delete objects first | No (recommended) |

## Examples

### Basic Usage

```bash
aws s3 rb s3://s3-r-w --force
```

### Advanced Usage

```bash
aws s3 rb s3://s3-r-w --force --region ap-east-1
```

## Expected Output

'remove bucket from s3-r-w: successfully removed bucket'.

## Related

- [[commands/aws-s3-ls-list]]
- [[procedures/Delete-S3-Bucket-for-Takeover]]
