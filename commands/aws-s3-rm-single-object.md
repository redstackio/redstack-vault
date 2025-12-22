---
type: command
executor: bash
data: 'aws s3 rm s3://$_BUCKET_NAME/$_OBJECT_KEY'
platforms:
  - Cloud
tags:
  - aws
  - s3
  - delete
verified: true
validated: true
---

# aws-s3-rm-single-object

## Command

```bash
aws s3 rm s3://$_BUCKET_NAME/$_OBJECT_KEY
```

## Description

Deletes a single object from an S3 bucket using the AWS CLI. This is a targeted removal operation suitable for eliminating specific files during data destruction or cleanup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BUCKET_NAME | The name of the target S3 bucket | Yes |
| $_OBJECT_KEY | The key (path) of the object to delete, e.g., folder/file.txt | Yes |

## Examples

### Basic Usage

```bash
aws s3 rm s3://my-bucket/documents/secret.txt
```

### Advanced Usage

```bash
aws s3 rm s3://my-bucket/logs/error.log --debug
```

## Expected Output

Successful deletion outputs a confirmation:
```
delete: s3://my-bucket/documents/secret.txt
```
If the object does not exist:
```
NoSuchKey: The specified key does not exist.
```

## Related

- [[procedures/Delete-Objects-from-AWS-S3-Bucket]]
- [[tools/aws-cli]]
