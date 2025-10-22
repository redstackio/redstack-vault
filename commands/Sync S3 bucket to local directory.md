---
id: 084f9b11-43a4-4a6c-9f65-2c072b86046b
name: Sync S3 bucket to local directory
type: command
executor: bash
data: aws s3 sync s3://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud/ . --no-sign-request
  --region us-west-2
output: null
created_at: '2023-04-06T03:55:52.816078+00:00'
updated_at: '2023-04-06T03:55:52.823192+00:00'
---

# Sync S3 bucket to local directory

```bash
aws s3 sync s3://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud/ . --no-sign-request --region us-west-2
```
