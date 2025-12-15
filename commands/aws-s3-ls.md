---
id: cmd-uuid-001
data: aws s3 ls
tags:
  - aws
  - cloud
type: command
output: null
executor: bash
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.056Z'
verified: false
validated: true
submitted: true
---
# aws-s3-ls

## Command

```bash
aws s3 ls
```

## Description

Lists all S3 buckets owned by the authenticated AWS account, used to verify access permissions with stolen credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Lists buckets in default region | No |
| `--region` | Specify AWS region | No |

## Examples

### Basic Usage

```bash
aws s3 ls
```

### Advanced Usage

```bash
aws s3 ls --region us-west-2
```

## Expected Output

A list of bucket names, e.g.,

```
2023-01-01 12:00:00 bucket1
2023-01-01 12:00:00 bucket2
```

## Related

- [[commands/aws-s3-cp]]
- [[procedures/Access-AWS-Resources-with-Stolen-Credentials]]
