---
id: cc88524e-ae63-449a-b64d-0007fad080c7
type: command
executor: bash
data: |
  aws s3 ls s3://$_BUCKET_NAME --region $_REGION
output: null
created_at: '2020-07-31T04:25:34.638162+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - AWS
  - S3
  - Reconnaissance
verified: true
validated: true
---

# aws-s3-list-bucket-contents

## Command

```bash
aws s3 ls s3://$_BUCKET_NAME --region $_REGION
```

## Description

This command lists the objects (files and folders) within a specified S3 bucket. It tests for public read access or permissions granted to the IAM credentials, useful for identifying exposed data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BUCKET_NAME | The name of the S3 bucket (e.g., "example-bucket"). | Yes |
| $_REGION | The AWS region of the bucket (e.g., "us-east-1"). | Yes |
| --no-sign-request | Use for anonymous access to public buckets (omit credentials). | No |

## Examples

### Basic Usage

```bash
aws s3 ls s3://example-bucket --region us-east-1
```

### Anonymous Public Access

```bash
aws s3 ls s3://public-bucket --region us-east-1 --no-sign-request
```

## Expected Output

A list of objects with sizes and dates if accessible:

```
2020-01-15 12:00:00     1024 config.json
2020-02-20 14:30:00    20480 backup.zip
```
If denied, an error like "An error occurred (AccessDenied) when calling the ListObjectsV2 operation: Access Denied" appears.

## Related

- [[procedures/Enumerate-AWS-S3-Buckets-and-Check-Public-Access]]
- [[commands/aws-s3-list-buckets]]
