---
id: cmd-uuid-4
data: 'aws s3 ls s3://██████████/███████/'
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
updated_at: '2025-12-14T17:28:58.499Z'
verified: false
validated: true
submitted: true
---
# aws-s3-ls-localhost-directory

## Command

```bash
aws s3 ls s3://██████████/███████/
```

## Description

Lists contents of a localhost or development subdirectory in the public bucket to uncover internal artifacts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://██████████/███████/` | Path to the localhost subdirectory | Yes |

## Examples

### Basic Usage

```bash
aws s3 ls s3://██████████/███████/
```

### Advanced Usage

```bash
aws s3 ls s3://██████████/███████/ --summarize
```

## Expected Output

Objects and subdirectories with DoD information.

## Related

- [[commands/aws-s3-ls-root]]
- [[procedures/Enumerate-S3-Directories-with-AWS-CLI]]
