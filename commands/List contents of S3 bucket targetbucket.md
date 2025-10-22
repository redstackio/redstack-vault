---
id: b737f75c-a4dc-4b0e-bd44-babcb9830c74
name: List contents of S3 bucket targetbucket
type: command
executor: bash
data: aws s3 ls s3://targetbucket --no-sign-request --region insert-region-here
output: null
created_at: '2023-04-06T03:55:52.768375+00:00'
updated_at: '2023-04-06T03:55:52.780272+00:00'
---

# List contents of S3 bucket targetbucket

```bash
aws s3 ls s3://targetbucket --no-sign-request --region insert-region-here
```
