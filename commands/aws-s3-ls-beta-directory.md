---
id: cmd-uuid-3
data: 'aws s3 ls s3://███████/███████████████/'
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
updated_at: '2025-12-14T17:28:58.502Z'
verified: false
validated: true
submitted: true
---
# aws-s3-ls-beta-directory

## Command

```bash
aws s3 ls s3://███████/███████████████/
```

## Description

Enumerates files in a beta testing subdirectory of a public S3 bucket, exposing development-related DoD data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://███████/███████████████/` | Path to the beta subdirectory | Yes |

## Examples

### Basic Usage

```bash
aws s3 ls s3://███████/███████████████/
```

### Advanced Usage

```bash
aws s3 ls s3://███████/███████████████/ --page-size 1000
```

## Expected Output

Directory listing with sensitive files visible.

## Related

- [[commands/aws-s3-ls-root]]
- [[procedures/Enumerate-S3-Directories-with-AWS-CLI]]
