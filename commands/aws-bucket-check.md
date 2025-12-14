---
data: aws s3api head-bucket --bucket storybook.lystit.com 2>&1 | grep 'NoSuchBucket'
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
updated_at: '2025-12-14T04:39:01.899Z'
id: a348fe4d-3606-484b-8c21-4c98d54bca87
verified: false
validated: true
submitted: true
---
# aws-bucket-check

## Command

```bash
aws s3api head-bucket --bucket storybook.lystit.com 2>&1 | grep 'NoSuchBucket'
```

## Description

Attempts to access an S3 bucket head to check if it exists; grep for NoSuchBucket confirms unclaimed status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--bucket` | S3 bucket name | Yes |

## Examples

### Basic Usage

```bash
aws s3api head-bucket --bucket storybook.lystit.com
```

### Advanced Usage

```bash
aws s3api head-bucket --bucket storybook.lystit.com 2>&1 | grep 'NoSuchBucket'
```

## Expected Output

'NoSuchBucket' error if unclaimed.

## Related

- [[Related Procedure: Discover Dangling CNAME Record]]
