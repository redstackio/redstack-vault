---
id: 9e9ef784-73bd-450a-911e-fc0c771e7b7c
name: Sync S3 bucket content to local directory
type: command
executor: bash
data: aws s3 sync s3://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud/ . --no-sign-request
  --region us-west-2
output: null
created_at: '2023-04-06T03:55:53.626520+00:00'
updated_at: '2023-04-06T03:55:53.633905+00:00'
---

# Sync S3 bucket content to local directory

```bash
aws s3 sync s3://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud/ . --no-sign-request --region us-west-2
```
