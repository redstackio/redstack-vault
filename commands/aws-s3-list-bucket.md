---
data: 'aws s3 ls s3://rocketchatbuild'
tags:
  - recon
  - s3
type: command
output: >-
  Error: 'An error occurred (NoSuchBucket) when calling the ListObjects
  operation: The specified bucket does not exist'
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.017Z'
id: 823223c6-2e1c-497f-9304-385d6b664b28
verified: false
validated: true
submitted: true
---
# aws-s3-list-bucket

## Command

```bash
aws s3 ls s3://rocketchatbuild
```

## Description

Lists objects in the specified S3 bucket, used to check existence and reveal unclaimed status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://rocketchatbuild` | The bucket name to list | Yes |

## Examples

### Basic Usage

```bash
aws s3 ls s3://rocketchatbuild
```

### Advanced Usage

```bash
aws s3 ls s3://rocketchatbuild --recursive
```

## Expected Output

For unclaimed bucket: NoSuchBucket error; for existing: list of objects.

## Related

- [[Related Procedure: Check-S3-Bucket-Existence-with-AWS-CLI]]
