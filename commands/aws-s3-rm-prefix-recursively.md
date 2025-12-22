---
type: command
executor: bash
data: 'aws s3 rm s3://$_BUCKET_NAME/$_PREFIX/ --recursive'
platforms:
  - Cloud
tags:
  - aws
  - s3
  - delete
  - recursive
verified: true
validated: true
---

# aws-s3-rm-prefix-recursively

## Command

```bash
aws s3 rm s3://$_BUCKET_NAME/$_PREFIX/ --recursive
```

## Description

Recursively deletes all objects under a specified prefix in an S3 bucket, effectively emptying a folder or the entire bucket if prefix is root. Ideal for large-scale data destruction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BUCKET_NAME | The name of the target S3 bucket | Yes |
| $_PREFIX | The prefix path for recursion, e.g., "folder/" or empty for root | Yes |
| --recursive | Flag to delete all objects under the prefix | Built-in |

## Examples

### Basic Usage

```bash
aws s3 rm s3://my-bucket/backups/ --recursive
```

### Advanced Usage

```bash
aws s3 rm s3://my-bucket/ --recursive
```

## Expected Output

Multiple confirmation lines, one per object:
```
delete: s3://my-bucket/backups/file1.txt
delete: s3://my-bucket/backups/file2.txt
...
```
No output if prefix is empty after deletion.

## Related

- [[procedures/Delete-Objects-from-AWS-S3-Bucket]]
- [[tools/aws-cli]]
