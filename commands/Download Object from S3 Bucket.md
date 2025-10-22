---
id: 07f79b4e-406f-4398-ae51-f599b4a6b7a3
name: Download Object from S3 Bucket
type: command
executor: bash
data: aws s3api get-object --bucket name --key object-name download-file-location
output: null
created_at: '2023-04-06T03:56:11.135089+00:00'
updated_at: '2023-04-10T20:19:54.016757+00:00'
---

# Download Object from S3 Bucket

```bash
aws s3api get-object --bucket name --key object-name download-file-location
```
