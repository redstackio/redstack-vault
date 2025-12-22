---
data: 'aws s3 ls s3://s3-r-w'
tags:
  - aws
  - s3
  - list
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.032Z'
id: 6cd79c7e-9ef8-4771-85c5-6e90674eddfb
verified: false
validated: true
submitted: true
---
---

# aws-s3-ls-list

## Command

```bash
aws s3 ls s3://s3-r-w
```

## Description

Lists objects in the specified S3 bucket, verifying public list access and uploaded contents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| s3://s3-r-w | Target S3 bucket URI | Yes |

## Examples

### Basic Usage

```bash
aws s3 ls s3://s3-r-w
```

### Advanced Usage

```bash
aws s3 ls s3://s3-r-w --recursive
```

## Expected Output

Listing of files: '2023-10-01 12:00:00     1024 dinesh.jpg'.

## Related

- [[commands/aws-s3-cp-upload]]
- [[procedures/List-Contents-of-S3-Bucket]]
