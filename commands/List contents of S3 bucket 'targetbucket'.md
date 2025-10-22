---
id: 15e55786-aaf7-4586-8b42-84e615790792
name: List contents of S3 bucket 'targetbucket'
type: command
executor: bash
data: aws s3 ls s3://targetbucket --no-sign-request --region insert-region-here
output: null
created_at: '2023-04-06T03:55:53.585420+00:00'
updated_at: '2023-04-06T03:55:53.600463+00:00'
---

# List contents of S3 bucket 'targetbucket'

```bash
aws s3 ls s3://targetbucket --no-sign-request --region insert-region-here
```
