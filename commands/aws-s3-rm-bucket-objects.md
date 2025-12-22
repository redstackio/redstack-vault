---
type: command
executor: bash
data: 'aws s3 rm s3://$_BUCKET_NAME/$_OBJECT_KEY1 s3://$_BUCKET_NAME/$_OBJECT_KEY2'
platforms:
  - Cloud
tags:
  - aws
  - s3
  - delete
  - bulk
verified: true
validated: true
---

# aws-s3-rm-bucket-objects

## Command

```bash
aws s3 rm s3://$_BUCKET_NAME/$_OBJECT_KEY1 s3://$_BUCKET_NAME/$_OBJECT_KEY2
```

## Description

Deletes multiple specified objects from an S3 bucket in one command. Useful for removing a set of known files without recursion, such as cleaning up specific logs or documents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BUCKET_NAME | The name of the target S3 bucket | Yes |
| $_OBJECT_KEY1 | The key of the first object to delete | Yes |
| $_OBJECT_KEY2 | The key of the second object to delete (extend for more) | Yes |

## Examples

### Basic Usage

```bash
aws s3 rm s3://my-bucket/log1.txt s3://my-bucket/log2.txt
```

### Advanced Usage

```bash
aws s3 rm s3://my-bucket/docs/file1.pdf s3://my-bucket/docs/file2.pdf s3://my-bucket/docs/file3.pdf
```

## Expected Output

Confirmation for each deletion:
```
delete: s3://my-bucket/log1.txt
delete: s3://my-bucket/log2.txt
```
Errors appear per failed object.

## Related

- [[procedures/Delete-Objects-from-AWS-S3-Bucket]]
- [[tools/aws-cli]]
