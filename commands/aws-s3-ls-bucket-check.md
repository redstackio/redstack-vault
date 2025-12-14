---
data: 'aws s3 ls s3://$BUCKET_NAME'
tags:
  - aws
  - s3
  - check
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.565Z'
id: c9e0561f-6cd0-48de-a59a-0dcedb8015b6
verified: false
validated: true
submitted: true
---
# aws-s3-ls-bucket-check

## Command

```bash
aws s3 ls s3://media.vine.co
```

## Description

Attempts to list contents of an S3 bucket to verify existence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://$BUCKET_NAME` | Bucket URI | Yes |

## Examples

### Basic Usage

```bash
aws s3 ls s3://media.vine.co
```

### Advanced Usage

```bash
aws s3 ls s3://media.vine.co --region us-east-1
```

## Expected Output

Error: "NoSuchBucket" if unclaimed.

## Related

- [[Related Procedure: Verify-Unclaimed-AWS-S3-Bucket]]
