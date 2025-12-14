---
id: cmd-uuid-4
data: 'aws s3 mb s3://ws-bimedb-com'
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
updated_at: '2025-12-14T05:32:23.748Z'
verified: false
validated: true
submitted: true
---
# aws-s3-mb-create

## Command

```bash
aws s3 mb s3://ws-bimedb-com
```

## Description

This command creates a new S3 bucket, claiming the name if unowned.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None specific | Bucket name in URI | Yes |

## Examples

### Basic Usage

```bash
aws s3 mb s3://my-bucket
```

## Expected Output

"make_bucket: my-bucket".

## Related

- [[Related Procedure: Verify-and-Claim-Unclaimed-S3-Bucket]]
