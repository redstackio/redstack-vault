---
type: command
executor: bash
data: 'aws s3 ls s3://$_BUCKET_NAME/ --no-sign-request --region $_REGION'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - s3
  - reconnaissance
verified: true
validated: true
---

# aws-s3-ls-bucket-no-auth

## Command

```bash
aws s3 ls s3://$_BUCKET_NAME/ --no-sign-request --region $_REGION
```

## Description

Lists objects in a public S3 bucket without AWS authentication, useful for checking exposure during cloud asset discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BUCKET_NAME | The target S3 bucket name (e.g., targetbucket) | Yes |
| $_REGION | The AWS region of the bucket (e.g., us-west-2) | Yes |
| --no-sign-request | Bypasses authentication for public buckets | Built-in |
| --region | Specifies the S3 region | Built-in |

## Examples

### Basic Usage

```bash
aws s3 ls s3://flaws.cloud/ --no-sign-request --region us-west-2
```

### Advanced Usage

```bash
aws s3 ls s3://$_BUCKET_NAME/ --no-sign-request --region $_REGION --recursive
```

## Expected Output

```
2023-01-01 12:00:00     1234 example-file.txt
PRE docs/
```

Lists keys, sizes, and dates; empty or AccessDenied indicates no public access.

## Related

- [[procedures/List-Files-in-S3-Bucket]]
- [[tools/AWS-CLI]]
