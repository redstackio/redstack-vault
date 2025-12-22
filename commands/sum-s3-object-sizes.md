---
id: 308c3b24-6f1a-4df6-bc37-c9d1e73cac6f
name: sum-s3-object-sizes
type: command
executor: bash
data: >-
  grep -v -E "(Bucket: |Prefix: |LastWriteTime|^$|--)" | awk 'BEGIN
  {total=0}{total+=$3}END{print total/1024/1024" MB"}'
output: null
created_at: '2023-04-06T03:55:53.656037+00:00'
updated_at: '2023-04-06T03:55:53.663167+00:00'
platforms:
  - AWS
tags:
  - aws
  - s3
  - calculation
verified: true
validated: true
---

# sum-s3-object-sizes

## Command

```bash
grep -v -E "(Bucket: |Prefix: |LastWriteTime|^$|--)" | awk 'BEGIN {total=0}{total+=$3}END{print total/1024/1024" MB"}'
```

## Description

This command processes the output from an AWS S3 ls command (piped input) to filter out non-object lines and calculate the total size of all listed files in megabytes. It is used post-enumeration to quickly summarize data volume in public S3 buckets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (piped input) | Output from 'aws s3 ls --recursive' containing object listings | Yes |
| -v -E "..." | Grep flags to exclude header, prefix, timestamp, empty, and separator lines | Built-in |
| awk script | Sums the size column ($3, in bytes) and converts to MB | Built-in |

## Examples

### Basic Usage

(Pipe from S3 ls):
```bash
aws s3 ls s3://example-bucket --recursive --no-sign | grep -v -E "(Bucket: |Prefix: |LastWriteTime|^$|--)" | awk 'BEGIN {total=0}{total+=$3}END{print total/1024/1024" MB"}'
```

### Advanced Usage

(From file):
```bash
cat objects.txt | grep -v -E "(Bucket: |Prefix: |LastWriteTime|^$|--)" | awk 'BEGIN {total=0}{total+=$3}END{print total/1024/1024" MB"}'
```

## Expected Output

A single line with the total size:

`154.25 MB`

(Or `0 MB` if no objects or empty bucket.)

## Related

- [[procedures/Enumerate-S3-Bucket-Size]]
- [[commands/aws-s3-ls-recursive-no-sign]]
