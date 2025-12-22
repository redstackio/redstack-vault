---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: 'aws s3 mb s3://$1 --region us-east-1'
tags:
  - aws
  - s3
  - create
type: command
output: 'make_bucket: legacy-bucket'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:51:10.862Z'
verified: false
validated: true
submitted: true
---
# aws-s3-mb-bucket

## Command

```bash
aws s3 mb s3://legacy-bucket --region us-east-1
```

## Description

Creates a new S3 bucket, claiming it if the name is available, as part of subdomain takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://bucket` | The S3 URI with bucket name | Yes |
| `--region` | AWS region for the bucket (us-east-1 for global) | Yes |

## Examples

### Basic Usage

```bash
aws s3 mb s3://legacy-bucket --region us-east-1
```

### Advanced Usage

```bash
aws s3 mb s3://legacy-bucket --region us-east-1 --no-verify-ssl
```

## Expected Output

Success message: 'make_bucket: legacy-bucket' if created.

## Related

- [[Related Procedure: Verify-and-Claim-Unclaimed-S3-Bucket]]
