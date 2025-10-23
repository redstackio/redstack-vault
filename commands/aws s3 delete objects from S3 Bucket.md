---
id: 16d93609-c602-48d0-9eb1-1e2897decbbb
name: aws s3 delete objects from S3 Bucket
type: command
executor: bash
data: 'aws s3 rm s3://$AWS_S3_BUCKET/$OBJECT

  '
output: aws s3 rm s3://redstack.io-s3bucket/folder-object
created_at: '2020-07-31T04:25:24.036341+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws s3 delete objects from S3 Bucket

```bash
aws s3 rm s3://$AWS_S3_BUCKET/$OBJECT

```

## Expected Output

```
aws s3 rm s3://redstack.io-s3bucket/folder-object
```


