---
id: 4ab0c904-04f7-4c62-9ac4-e8d63b638374
name: Syncing a Local Folder with a Bucket
type: command
executor: bash
data: 'aws s3 sync $FOLDER s3://$AWS_S3_BUCKET

  '
output: aws s3 sync target-folder s3://redstack.io-s3bucket
created_at: '2020-07-31T04:25:33.754089+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Syncing a Local Folder with a Bucket

```bash
aws s3 sync $FOLDER s3://$AWS_S3_BUCKET

```

## Expected Output

```
aws s3 sync target-folder s3://redstack.io-s3bucket
```


