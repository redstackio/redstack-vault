---
id: 123e4567-e89b-12d3-a456-426614174004
name: aws-s3-ls-list-buckets
type: command
executor: bash
data: 'aws s3 ls s3://bucket-name'
output: '2023-10-01 00:00:00   0 poc.txt'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.861Z'
platforms:
  - AWS
  - Linux
  - macOS
tags:
  - aws
  - s3
verified: false
validated: true
submitted: true
---

# aws s3 ls list-buckets

## Command

```bash
aws s3 ls s3://bucket-name
```

## Description

Lists objects in an S3 bucket to verify ownership and contents post-creation in takeover attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://bucket-name` | Target bucket path | Yes |

## Examples

### Basic Usage

```bash
aws s3 ls s3://abandoned-bucket-name
```

### Advanced Usage

```bash
aws s3 ls s3://abandoned-bucket-name/ --recursive
```

## Expected Output

Timestamped list of files, e.g., "2023-10-01 00:00:00   0 poc.txt".

## Related

- [[commands/aws-s3-mb-create-bucket]]
- [[procedures/Reclaim-Abandoned-S3-Bucket-via-Global-Namespacing]]
