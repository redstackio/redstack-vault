---
id: cmd-uuid-1
data: 'aws s3 ls s3://███/'
tags:
  - aws
  - s3
  - enumeration
type: command
output: null
executor: bash
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.506Z'
verified: false
validated: true
submitted: true
---
# aws-s3-ls-root

## Command

```bash
aws s3 ls s3://███/
```

## Description

Lists all objects and prefixes in the root directory of a public AWS S3 bucket, used to enumerate initial contents without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://███/` | Path to the root of the redacted bucket | Yes |

## Examples

### Basic Usage

```bash
aws s3 ls s3://███/
```

### Advanced Usage

```bash
aws s3 ls s3://███/ --recursive
```

## Expected Output

A list of directories and files, e.g.,

```
2023-01-01 12:00:00     1024 admin/
2023-01-01 12:00:00     2048 production/
```

## Related

- [[commands/aws-s3-ls-admin-directory]]
- [[procedures/Enumerate-S3-Directories-with-AWS-CLI]]
