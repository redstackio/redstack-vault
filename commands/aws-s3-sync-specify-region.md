---
id: abfa61c6-3653-4b5b-af57-8a6007cce060
name: aws-s3-sync-specify-region
type: command
executor: bash
data: |
  aws s3 sync . s3://$AWS_S3_BUCKET --region $AWS_REGION
output: null
created_at: '2020-07-31T04:25:33.754298+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - AWS
  - S3
  - Sync
  - Region
verified: true
validated: true
---

# aws-s3-sync-specify-region

## Command

```bash
aws s3 sync . s3://$AWS_S3_BUCKET --region $AWS_REGION
```

## Description

Synchronizes the current directory to an S3 bucket while specifying the AWS region. Ideal for multi-region setups to ensure operations target the correct endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| . | Current directory as source | Built-in |
| $AWS_S3_BUCKET | Target S3 bucket name | Yes |
| --region $AWS_REGION | AWS region (e.g., us-east-1) | Yes |

## Examples

### Basic Usage

```bash
aws s3 sync . s3://my-bucket --region us-west-2
```

### Advanced Usage

```bash
aws s3 sync . s3://my-bucket --region us-west-2 --include "*.log"
```

## Expected Output

Upload progress with region confirmation:

```
upload: file1.log to s3://my-bucket/file1.log
Completed 1 part(s) with ... file(s) remaining
```

## Related

- [[procedures/AWS-Sync-Folder-with-S3-Bucket]]
- [[commands/aws-s3-sync-local-folder]]
