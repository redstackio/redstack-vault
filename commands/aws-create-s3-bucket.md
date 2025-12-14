---
id: 123e4567-e89b-12d3-a456-426614174006
name: aws-create-s3-bucket
type: command
executor: bash
data: 'aws s3 mb s3://users.tweetdeck.com --region us-east-1'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.507Z'
platforms:
  - Linux
  - macOS
tags:
  - aws
  - s3
verified: false
validated: true
submitted: true
---

# aws-create-s3-bucket

## Command

```bash
aws s3 mb s3://users.tweetdeck.com --region us-east-1
```

## Description

Creates an S3 bucket for subdomain takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `mb` | Make bucket | Yes |
| `s3://users.tweetdeck.com` | Bucket name | Yes |
| `--region us-east-1` | AWS region | Yes |

## Examples

### Basic Usage

```bash
aws s3 mb s3://example.com --region us-east-1
```

## Expected Output

"make_bucket: example.com"

## Related

- [[Related Procedure]]
