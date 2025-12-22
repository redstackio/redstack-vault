---
type: command
executor: bash
data: 'aws s3 rb s3://$_BUCKET_NAME'
tags:
  - aws
  - s3
  - deletion
platforms:
  - AWS
verified: true
validated: true
---

# aws-s3-rm-bucket

## Command

```bash
aws s3 rb s3://$_BUCKET_NAME
```

## Description

This command removes an AWS S3 bucket using the AWS CLI. It only succeeds if the bucket is empty; otherwise, it fails with a BucketNotEmpty error. Use this for cleanup of unused empty buckets in red team exercises.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| s3://$_BUCKET_NAME | The name of the S3 bucket to delete (e.g., s3://my-bucket) | Yes |
| rb | Recursive bucket removal flag (built-in for s3 rb) | Yes |

## Examples

### Basic Usage

```bash
aws s3 rb s3://my-empty-bucket
```

### With Region Specification

```bash
aws s3 rb s3://my-empty-bucket --region us-west-2
```

## Expected Output

On success:
```
remove_bucket: my-empty-bucket
```

On failure (non-empty):
```
An error occurred (BucketNotEmpty) when calling the DeleteBucket operation: The bucket you tried to delete is not empty
```

## Related

- [[commands/aws-s3-rm-bucket-force]]
- [[procedures/aws-delete-s3-bucket]]
