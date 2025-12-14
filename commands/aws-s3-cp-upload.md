---
id: cmd-uuid-5
data: 'aws s3 cp test.html s3://ws-bimedb-com/'
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
updated_at: '2025-12-14T05:32:23.745Z'
verified: false
validated: true
submitted: true
---
# aws-s3-cp-upload

## Command

```bash
aws s3 cp test.html s3://ws-bimedb-com/
```

## Description

This command uploads a local file to an S3 bucket to verify control.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None specific | Source and destination | Yes |

## Examples

### Basic Usage

```bash
aws s3 cp file.txt s3://bucket/
```

## Expected Output

"upload: file.txt to s3://bucket/file.txt".

## Related

- [[Related Procedure: Verify-and-Claim-Unclaimed-S3-Bucket]]
