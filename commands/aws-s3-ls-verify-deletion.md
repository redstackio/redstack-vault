---
id: cmd-uuid-4
data: 'aws s3 ls s3://affirm-prod-www-cms█████████'
tags:
  - verification
  - s3
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.706Z'
verified: false
validated: true
submitted: true
---
# aws-s3-ls-verify-deletion

## Command

```bash
aws s3 ls s3://affirm-prod-www-cms█████████
```

## Description

Lists objects in the S3 bucket to verify its deletion post-cleanup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ls | List bucket contents | Yes |
| s3://bucket | Bucket URI | Yes |

## Examples

### Basic Usage

```bash
aws s3 ls s3://affirm-prod-www-cms█████████
```

### Advanced Usage

```bash
aws s3 ls s3://affirm-prod-www-cms█████████ --region us-east-1
```

## Expected Output

An error occurred (NoSuchBucket) when calling the ListObjectsV2 operation: The specified bucket does not exist

## Related

- [[Related Procedure|procedures/Claim-Dangling-S3-Bucket]]
