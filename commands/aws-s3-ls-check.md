---
id: cmd-uuid-3
data: 'aws s3 ls s3://ws-bimedb-com --no-sign-request'
tags:
  - aws
  - s3
  - cloud
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.753Z'
verified: false
validated: true
submitted: true
---
# aws-s3-ls-check

## Command

```bash
aws s3 ls s3://ws-bimedb-com --no-sign-request
```

## Description

This command attempts to list objects in an S3 bucket without authentication to check if it's publicly accessible or unclaimed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--no-sign-request` | Anonymous access | Yes |

## Examples

### Basic Usage

```bash
aws s3 ls s3://bucket-name --no-sign-request
```

## Expected Output

Error if unclaimed, e.g., "An error occurred (NoSuchBucket) when calling the ListBuckets operation".

## Related

- [[Related Procedure: Verify-and-Claim-Unclaimed-S3-Bucket]]
