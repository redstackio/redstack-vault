---
id: db0b46a3-d2f0-4346-860e-ea76fac9d4bc
name: aws s3 copy folder to bucket recursively
type: command
executor: bash
data: 'aws s3 cp $FOLDER s3://$AWS_S3_BUCKET/ --recursive

  '
output: null
created_at: '2020-07-31T04:25:22.639440+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# aws s3 copy folder to bucket recursively

```bash
aws s3 cp $FOLDER s3://$AWS_S3_BUCKET/ --recursive

```
