---
id: 0b720a01-dd0d-4de3-b393-5da0cea47b23
type: command
executor: bash
data: |
  aws s3 ls
output: null
created_at: '2020-07-14T19:06:15.095784+00:00'
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

# aws-s3-list-buckets

## Command

```bash
aws s3 ls
```

## Description

This command lists all S3 buckets accessible to the currently configured AWS credentials. It is used for initial discovery of storage resources in an AWS account during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters required; uses default region (us-east-1) and configured credentials. | No |
| --region | Specify AWS region (e.g., eu-west-1) if not default. | No |

## Examples

### Basic Usage

```bash
aws s3 ls
```

### With Region

```bash
aws s3 ls --region us-west-2
```

## Expected Output

A list of bucket names with creation dates, or an empty list if no access:

```
2020-01-15 12:00:00 example-bucket1
2020-02-20 14:30:00 example-bucket2
```
If access is denied, output will show an error like "An error occurred (AccessDenied) when calling the ListBuckets operation".

## Related

- [[procedures/Enumerate-AWS-S3-Buckets-and-Check-Public-Access]]
- [[commands/aws-s3-list-bucket-contents]]
