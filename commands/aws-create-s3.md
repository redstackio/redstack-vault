---
id: cmd-uuid-2
data: 'aws s3 mb s3://dangling-bucket-name --region us-east-1'
tags:
  - aws
  - cloud
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.057Z'
verified: false
validated: true
submitted: true
---
# aws-create-s3

## Command

```bash
aws s3 mb s3://dangling-bucket-name --region us-east-1
```

## Description

Creates an S3 bucket with a specific name to claim a dangling DNS resource.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://dangling-bucket-name` | Bucket name | Yes |
| `--region` | AWS region | Yes |

## Examples

### Basic Usage

```bash
aws s3 mb s3://mybucket
```

### Advanced Usage

```bash
aws s3 mb s3://mybucket --region eu-west-1
```

## Expected Output

'make_bucket: mybucket' confirmation.

## Related

- [[Related Procedure]]
