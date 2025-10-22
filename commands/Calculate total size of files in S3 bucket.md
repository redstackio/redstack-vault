---
id: bf39031c-8403-447f-b347-cbd89ea1f551
name: Calculate total size of files in S3 bucket
type: command
executor: bash
data: 's3 ls s3://<bucketname> --recursive  | grep -v -E "(Bucket: |Prefix: |LastWriteTime|^$|--)"
  | awk ''BEGIN {total=0}{total+=$3}END{print total/1024/1024" MB"}'''
output: null
created_at: '2023-04-06T03:55:53.656154+00:00'
updated_at: '2023-04-06T03:55:53.663296+00:00'
---

# Calculate total size of files in S3 bucket

```bash
s3 ls s3://<bucketname> --recursive  | grep -v -E "(Bucket: |Prefix: |LastWriteTime|^$|--)" | awk 'BEGIN {total=0}{total+=$3}END{print total/1024/1024" MB"}'
```
