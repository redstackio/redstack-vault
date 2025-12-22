---
id: 92259d66-7742-47b6-9b79-038fe559e27a
name: aws s3 copy current folder contents to bucket recursively
type: command
executor: bash
data: |
  aws s3 cp . s3://$AWS_S3_BUCKET/$FOLDER --recursive --region $AWS_REGION
output: null
created_at: '2020-07-31T04:25:22.639762+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - AWS
  - Linux
tags:
  - aws
  - s3
  - upload
  - recursive
verified: true
validated: true
---

# aws s3 copy current folder contents to bucket recursively

## Command

```bash
aws s3 cp . s3://$AWS_S3_BUCKET/$FOLDER --recursive --region $AWS_REGION
```

## Description

Uploads all files from the current directory recursively to a folder in an S3 bucket, specifying the AWS region for targeted operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| . | Current directory (implied source) | Yes |
| $AWS_S3_BUCKET | Target S3 bucket name | Yes |
| $FOLDER | Destination folder in bucket | Yes |
| --recursive | Include all files and subdirs | Yes |
| --region | AWS region (e.g., us-east-1) | Yes |

## Examples

### Basic Usage

```bash
aws s3 cp . s3://my-bucket/current/ --recursive --region us-east-1
```

### Advanced Usage

```bash
aws s3 cp . s3://my-bucket/exfil/ --recursive --region us-west-2 --include "*.conf"
```

## Expected Output

Upload summaries for each file, with overall completion status.

## Related

- [[procedures/aws-copy-files-or-folder-to-s3-bucket]]
