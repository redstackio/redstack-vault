---
id: abfa61c6-3653-4b5b-af57-8a6007cce060
name: aws s3 sync s3 bucket with region
type: command
executor: bash
data: 'aws s3 sync . s3://$AWS_S3_BUCKET --region $AWS_REGION

  '
output: aws s3 sync . s3://practicalaws.com --region us-east-1
created_at: '2020-07-31T04:25:33.754298+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws s3 sync s3 bucket with region

```bash
aws s3 sync . s3://$AWS_S3_BUCKET --region $AWS_REGION

```

## Expected Output

```
aws s3 sync . s3://practicalaws.com --region us-east-1
```


