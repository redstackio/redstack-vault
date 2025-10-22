---
id: 92259d66-7742-47b6-9b79-038fe559e27a
name: aws s3 copy current folder contents to bucket recursively
type: command
executor: bash
data: 'aws s3 cp . s3://$AWS_S3_BUCKET/$FOLDER --recursive --region $AWS_REGION

  '
output: null
created_at: '2020-07-31T04:25:22.639762+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws s3 copy current folder contents to bucket recursively

```bash
aws s3 cp . s3://$AWS_S3_BUCKET/$FOLDER --recursive --region $AWS_REGION

```
