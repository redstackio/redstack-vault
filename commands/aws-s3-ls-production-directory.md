---
id: cmd-uuid-5
data: 'aws s3 ls s3://██████████/████/'
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
updated_at: '2025-12-14T17:28:58.495Z'
verified: false
validated: true
submitted: true
---
# aws-s3-ls-production-directory

## Command

```bash
aws s3 ls s3://██████████/████/
```

## Description

Enumerates a production subdirectory to access live sensitive data in the misconfigured bucket.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://██████████/████/` | Path to the production subdirectory | Yes |

## Examples

### Basic Usage

```bash
aws s3 ls s3://██████████/████/
```

### Advanced Usage

```bash
aws s3 ls s3://██████████/████/ --no-sign-request
```

## Expected Output

List of media and document files.

## Related

- [[commands/aws-s3-ls-root]]
- [[procedures/Enumerate-S3-Directories-with-AWS-CLI]]
