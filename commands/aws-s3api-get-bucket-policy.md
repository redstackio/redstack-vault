---
id: 3536d716-ec0d-45cc-ad12-1f6b5e7e1049
name: aws-s3api-get-bucket-policy
type: command
executor: bash
data: aws s3api get-bucket-policy --bucket $_BUCKET_NAME
output: null
created_at: '2023-04-06T03:56:11.016598+00:00'
updated_at: '2023-04-10T20:20:44.638169+00:00'
platforms:
  - AWS
tags:
  - cloud
  - s3
  - enumeration
verified: true
validated: true
---

# aws-s3api-get-bucket-policy

## Command

```bash
aws s3api get-bucket-policy --bucket $_BUCKET_NAME
```

## Description

This command retrieves the policy document attached to an AWS S3 bucket using the AWS CLI's s3api subcommand. It is used during cloud enumeration to inspect access controls and identify misconfigurations like public permissions. Requires AWS credentials with s3:GetBucketPolicy permission.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --bucket $_BUCKET_NAME | The name of the S3 bucket to retrieve the policy for (e.g., my-bucket) | Yes |
| --profile $_PROFILE | Optional AWS profile name from ~/.aws/config if using multiple credential sets | No |
| --region $_REGION | AWS region of the bucket (defaults to us-east-1 if not specified) | No |

## Examples

### Basic Usage

```bash
aws s3api get-bucket-policy --bucket example-bucket
```

### Advanced Usage

```bash
aws s3api get-bucket-policy --bucket example-bucket --region us-west-2 --profile my-aws-profile | jq '.'
```

## Expected Output

Successful execution returns a JSON response like:

```json
{
    "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"s3:GetObject\",\"Resource\":\"arn:aws:s3:::example-bucket/*\"}]}"
}
```

If no policy exists, it returns {"Policy": ""}. Errors include AccessDenied (insufficient permissions) or NoSuchBucket (invalid name). The policy string can be parsed with jq or similar for analysis.

## Related

- [[procedures/Enumerate-AWS-S3-Bucket-Policy]]
- [[tools/aws-cli]]
