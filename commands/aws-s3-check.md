---
id: cmd-002
data: >-
  aws s3api head-bucket --bucket $BUCKET_NAME 2>/dev/null || echo "Bucket
  available"
tags:
  - aws
  - cloud
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.194Z'
verified: false
validated: true
submitted: true
---
# aws-s3-check

## Command

```bash
aws s3api head-bucket --bucket $BUCKET_NAME 2>/dev/null || echo "Bucket available"
```

## Description

Checks if an AWS S3 bucket exists as part of validating a dangling DNS record for takeover potential.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--bucket` | S3 bucket name derived from DNS | Yes |
| `$BUCKET_NAME` | Variable for the target bucket | Yes |

## Examples

### Basic Usage

```bash
aws s3api head-bucket --bucket dangling-bucket 2>/dev/null || echo "Available"
```

### Advanced Usage

```bash
aws s3api head-bucket --bucket dangling-bucket --profile attacker-profile
```

## Expected Output

Error message if bucket exists (e.g., NoSuchBucket), or "Bucket available" if claimable.

## Related

- [[Related Procedure: Perform-AWS-Subdomain-Takeover]]
