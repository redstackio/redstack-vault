---
id: 6eae8ef7-ae21-48ba-a94c-deeb4fd2b59c
name: aws s3 delete contents of S3 Bucket recursively
type: command
executor: bash
data: 'aws s3 rm s3://$AWS_S3_BUCKET/$OBJECT --recursive

  '
output: aws s3 rm s3://fakeRedstackBucket/keyName --recursive
created_at: '2020-07-31T04:25:24.036665+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws s3 delete contents of S3 Bucket recursively

```bash
aws s3 rm s3://$AWS_S3_BUCKET/$OBJECT --recursive

```

## Expected Output

```
aws s3 rm s3://fakeRedstackBucket/keyName --recursive
```
