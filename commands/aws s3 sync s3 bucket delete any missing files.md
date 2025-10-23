---
id: 4781c25f-9c2f-413a-b188-d2a3e3b61e80
name: aws s3 sync s3 bucket delete any missing files
type: command
executor: bash
data: 'aws s3 sync . s3://$AWS_S3_BUCKET --region $AWS_REGION --delete

  '
output: aws s3 sync . s3://redstack.io-s3bucket --region us-east-1 --delete
created_at: '2020-07-31T04:25:33.754544+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws s3 sync s3 bucket delete any missing files

```bash
aws s3 sync . s3://$AWS_S3_BUCKET --region $AWS_REGION --delete

```

## Expected Output

```
aws s3 sync . s3://redstack.io-s3bucket --region us-east-1 --delete
```


