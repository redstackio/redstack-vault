---
id: f0a211e4-9564-4d80-aeb6-467976be9be9
name: aws-s3api-get-public-access-block
type: command
executor: bash
data: aws s3api get-public-access-block --bucket $_BUCKET_NAME
output: null
created_at: '2023-04-06T03:56:11.040510+00:00'
updated_at: '2023-04-10T20:20:12.207721+00:00'
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
tags:
  - cloud
  - enumeration
  - aws
verified: true
validated: true
---

# aws-s3api-get-public-access-block

## Command

```bash
aws s3api get-public-access-block --bucket $_BUCKET_NAME
```

## Description

This command retrieves the Public Access Block configuration for a specified S3 bucket using the AWS CLI's S3 API interface. It is used during cloud reconnaissance to check if public access to the bucket is restricted, helping identify misconfigurations that could lead to data exposure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--bucket` | The name of the S3 bucket to query (e.g., `my-bucket-name`) | Yes |
| `$_BUCKET_NAME` | Placeholder for the actual bucket name to substitute | Yes |

## Examples

### Basic Usage

```bash
aws s3api get-public-access-block --bucket example-bucket
```

### With AWS Profile

```bash
aws s3api get-public-access-block --bucket example-bucket --profile my-aws-profile
```

## Expected Output

A JSON object detailing the Public Access Block settings:

```json
{
    "PublicAccessBlockConfiguration": {
        "BlockPublicAcls": true,
        "IgnorePublicAcls": true,
        "BlockPublicPolicy": true,
        "RestrictPublicBuckets": true
    }
}
```

If the configuration is not set, it may return an empty or default response indicating no blocks are enforced.

## Related

- [[procedures/Enumerate-AWS-S3-Bucket-Public-Access-Block]]
- [[tools/AWS-CLI]]
