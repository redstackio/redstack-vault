---
id: 156b1cbc-8748-4a82-a29b-67b3ce2f24cf
name: Get object ACL from S3 bucket
type: command
executor: bash
data: aws s3api get-object-acl --bucket-name name --key object_name
output: null
created_at: '2023-04-06T03:56:11.089610+00:00'
updated_at: '2023-04-10T20:20:21.145437+00:00'
---

# Get object ACL from S3 bucket

```bash
aws s3api get-object-acl --bucket-name name --key object_name
```
