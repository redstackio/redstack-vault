---
id: cmd-uuid-2
data: 'aws s3 ls s3://████/██████/'
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
updated_at: '2025-12-14T17:28:58.504Z'
verified: false
validated: true
submitted: true
---
# aws-s3-ls-admin-directory

## Command

```bash
aws s3 ls s3://████/██████/
```

## Description

Lists contents of a specific subdirectory (e.g., admin) in a public S3 bucket to reveal sensitive administrative files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://████/██████/` | Path to the subdirectory in the redacted bucket | Yes |

## Examples

### Basic Usage

```bash
aws s3 ls s3://████/██████/
```

### Advanced Usage

```bash
aws s3 ls s3://████/██████/ --human-readable
```

## Expected Output

List of objects, e.g.,

```
2023-01-01 12:00:00   1.2 MiB manual.pdf
2023-01-01 12:00:00   500 KiB media/video.mp4
```

## Related

- [[commands/aws-s3-ls-root]]
- [[procedures/Enumerate-S3-Directories-with-AWS-CLI]]
