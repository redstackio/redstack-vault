---
id: cc88524e-ae63-449a-b64d-0007fad080c7
name: Listing the Content of a Bucket
type: command
executor: bash
data: 'aws s3 ls s3://$AWS_S3_BUCKET --region $AWS_REGION

  '
output: aws s3 ls s3://awsBucketName --region us-east-1
created_at: '2020-07-31T04:25:34.638162+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Listing the Content of a Bucket

```bash
aws s3 ls s3://$AWS_S3_BUCKET --region $AWS_REGION

```

## Expected Output

```
aws s3 ls s3://awsBucketName --region us-east-1
```
