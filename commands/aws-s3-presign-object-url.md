---
id: f7bbaea8-7d77-4bb8-ae26-aa47825e95df
name: aws-s3-presign-object-url
type: command
executor: bash
data: >-
  aws s3 presign s3://$_BUCKET_NAME/$_OBJECT_KEY --expires-in
  $_EXPIRATION_SECONDS
output: null
created_at: '2023-04-06T03:56:11.160448+00:00'
updated_at: '2023-04-10T20:20:44.978625+00:00'
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
tags:
  - cloud-aws
  - exfiltration
verified: true
validated: true
---

# aws-s3-presign-object-url

## Command

```bash
aws s3 presign s3://$_BUCKET_NAME/$_OBJECT_KEY --expires-in $_EXPIRATION_SECONDS
```

## Description

This command generates a pre-signed URL for an S3 object using the AWS CLI, allowing temporary HTTP access without additional authentication. It is used in exfiltration scenarios to provide time-bound access to sensitive data in S3 buckets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| s3://$_BUCKET_NAME/$_OBJECT_KEY | The S3 URI specifying the bucket and object key to presign (e.g., s3://mybucket/secrets.txt) | Yes |
| --expires-in $_EXPIRATION_SECONDS | Expiration time in seconds (e.g., 3600 for 1 hour, max 604800 for 7 days) | Yes |

## Examples

### Basic Usage

```bash
aws s3 presign s3://mybucket/document.pdf --expires-in 3600
```

### Advanced Usage

```bash
aws s3 presign s3://mybucket/secrets.txt --expires-in 605000 --region us-east-1
```

## Expected Output

A pre-signed HTTPS URL, such as:

```
https://mybucket.s3.amazonaws.com/document.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA.../20230406/us-east-1/s3/aws4_request&X-Amz-Date=20230406T120000Z&X-Amz-Expires=3600&X-Amz-Signature=abc123...&X-Amz-SignedHeaders=host&actor_id=...&user_id=...
```

This URL can be used immediately to download the object via curl or wget. If the command fails, check credentials and permissions (error like "AccessDenied").

## Related

- [[procedures/Generate-AWS-S3-Pre-Signed-URL-for-Exfiltration]]
