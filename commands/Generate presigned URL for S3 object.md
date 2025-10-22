---
id: f7bbaea8-7d77-4bb8-ae26-aa47825e95df
name: Generate presigned URL for S3 object
type: command
executor: bash
data: aws s3 presign s3://bucket-name/object-name --expires-in 605000
output: null
created_at: '2023-04-06T03:56:11.160448+00:00'
updated_at: '2023-04-10T20:20:44.978625+00:00'
---

# Generate presigned URL for S3 object

```bash
aws s3 presign s3://bucket-name/object-name --expires-in 605000
```
