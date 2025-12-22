---
id: 07f79b4e-406f-4398-ae51-f599b4a6b7a3
name: aws-s3api-get-object
type: command
executor: bash
data: >-
  aws s3api get-object --bucket $_BUCKET_NAME --key $_OBJECT_KEY
  $_LOCAL_FILE_PATH
output: null
created_at: '2023-04-06T03:56:11.135089+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - exfiltration
  - aws
  - s3
verified: true
validated: true
---

# aws-s3api-get-object

## Command

```bash
aws s3api get-object --bucket $_BUCKET_NAME --key $_OBJECT_KEY $_LOCAL_FILE_PATH
```

## Description

This command retrieves a specific object from an Amazon S3 bucket using the AWS CLI's low-level s3api interface. It is used in exfiltration scenarios to download files from compromised AWS accounts, authenticating via configured credentials and saving the object locally.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --bucket $_BUCKET_NAME | The name of the S3 bucket containing the object | Yes |
| --key $_OBJECT_KEY | The key (path/filename) of the object within the bucket | Yes |
| $_LOCAL_FILE_PATH | The local file path where the object will be saved | Yes |

## Examples

### Basic Usage

```bash
aws s3api get-object --bucket my-bucket --key documents/secrets.txt ./secrets.txt
```

### Advanced Usage

```bash
aws s3api get-object --bucket my-bucket --key logs/app.log --region us-west-2 ./app.log
```

## Expected Output

Upon success, the command outputs JSON metadata about the object (e.g., {"AcceptRanges": "bytes", "LastModified": "2023-...", "ContentLength": 1024, "ETag": "\"abc123...\""}) and saves the file to the specified path. No errors indicate successful download; check the local file for content verification.

## Related

- [[procedures/AWS-S3-Download-by-Authenticated-User]]
- [[tools/AWS-CLI]]
