---
type: command
executor: bash
data: 'aws s3 rb s3://$_BUCKET_NAME --force'
tags:
  - aws
  - s3
  - deletion
  - force
platforms:
  - AWS
verified: true
validated: true
---

# aws-s3-rm-bucket-force

## Command

```bash
aws s3 rb s3://$_BUCKET_NAME --force
```

## Description

This command force-removes an AWS S3 bucket, deleting all objects inside first, then the bucket. Ideal for complete cleanup in destructive scenarios or post-exploitation resource removal.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| s3://$_BUCKET_NAME | The name of the S3 bucket to delete (e.g., s3://practicalaws.com) | Yes |
| rb | Recursive bucket removal flag (built-in for s3 rb) | Yes |
| --force | Force deletion of non-empty bucket by removing objects first | Yes |

## Examples

### Basic Usage

```bash
aws s3 rb s3://my-nonempty-bucket --force
```

### With Region and Output Format

```bash
aws s3 rb s3://my-nonempty-bucket --force --region us-east-1 --output json
```

## Expected Output

On success (deleting objects and bucket):
```
delete: s3://my-nonempty-bucket/object1.txt
 delete: s3://my-nonempty-bucket/folder/
remove_bucket: my-nonempty-bucket
```

On failure (permissions):
```
An error occurred (AccessDenied) when calling the DeleteObject operation: Access Denied
```

## Related

- [[commands/aws-s3-rm-bucket]]
- [[procedures/aws-delete-s3-bucket]]
