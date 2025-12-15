---
id: 123e4567-e89b-12d3-a456-426614174003
data: 'aws s3 mb s3://bucket-name --region us-east-1'
tags:
  - aws
  - s3
type: command
output: 'make_bucket: bucket-name'
executor: bash
platforms:
  - AWS
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.239Z'
verified: false
validated: true
submitted: true
---
---
id: 123e4567-e89b-12d3-a456-426614174003
name: aws-s3-mb-create-bucket
type: command
executor: bash
data: |
  aws s3 mb s3://bucket-name --region us-east-1
output: make_bucket: bucket-name
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
platforms: ["AWS", "Linux", "macOS"]
tags: ["aws", "s3"]
---

# aws s3 mb create-bucket

## Command

```bash
aws s3 mb s3://bucket-name --region us-east-1
```

## Description

Creates a new S3 bucket with the specified name in the given region, exploiting global namespace if available. Used in bucket takeover scenarios to claim abandoned names.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://bucket-name` | The globally unique bucket name to create | Yes |
| `--region` | AWS region (e.g., us-east-1) | Yes |

## Examples

### Basic Usage

```bash
aws s3 mb s3://abandoned-mapbox-bucket --region us-east-1
```

### Advanced Usage

```bash
aws s3 mb s3://abandoned-mapbox-bucket --region us-east-1 --no-verify-ssl
```

## Expected Output

"make_bucket: abandoned-mapbox-bucket" if successful; error if name taken.

## Related

- [[commands/aws-s3-ls-list-buckets]]
- [[procedures/Reclaim-Abandoned-S3-Bucket-via-Global-Namespacing]]
