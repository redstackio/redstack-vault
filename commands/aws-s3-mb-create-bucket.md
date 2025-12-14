---
id: uuid-c1
data: 'aws s3 mb s3://delivery.yelp.com --region us-east-1'
tags:
  - aws-cli
  - s3
type: command
output: 'make_bucket: delivery.yelp.com'
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.134Z'
verified: false
validated: true
submitted: true
---
# aws-s3-mb-create-bucket

## Command

```bash
aws s3 mb s3://delivery.yelp.com --region us-east-1
```

## Description

Creates a new S3 bucket with the specified name in the given region, useful for claiming unclaimed resources in subdomain takeover attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://bucket-name` | The S3 URI for the bucket to create | Yes |
| `--region` | AWS region (e.g., us-east-1) | Yes |

## Examples

### Basic Usage

```bash
aws s3 mb s3://example.com --region us-east-1
```

### Advanced Usage

```bash
aws s3 mb s3://example.com --region us-west-2 --profile attacker-profile
```

## Expected Output

Confirmation message like "make_bucket: bucket-name" if successful; error if name is taken.

## Related

- [[Related Procedure: Create-Unclaimed-AWS-S3-Bucket]]
