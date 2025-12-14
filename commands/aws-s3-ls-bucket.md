---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: 'aws s3 ls s3://$1 --no-sign-request'
tags:
  - aws
  - s3
type: command
output: NoSuchBucket
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:51:10.864Z'
verified: false
validated: true
submitted: true
---
# aws-s3-ls-bucket

## Command

```bash
aws s3 ls s3://legacy-bucket --no-sign-request
```

## Description

Attempts to list contents of an S3 bucket anonymously to check if it's claimed or accessible publicly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://bucket` | The S3 URI of the bucket | Yes |
| `--no-sign-request` | Performs unsigned request for public/anonymous access | Yes |

## Examples

### Basic Usage

```bash
aws s3 ls s3://legacy-bucket --no-sign-request
```

### Advanced Usage

```bash
aws s3 ls s3://legacy-bucket --region us-west-2 --no-sign-request
```

## Expected Output

Error like 'NoSuchBucket' if unclaimed, or list of objects if public and claimed.

## Related

- [[Related Procedure: Verify-and-Claim-Unclaimed-S3-Bucket]]
