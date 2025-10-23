---
id: 5ffbb937-92ad-4764-9ef3-ca8ff3bbc8aa
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:52.848953+00:00'
updated_at: '2023-04-06T03:55:52.856312+00:00'
---

# Code Snippet 5ffbb937

**Language**: Powershell

```powershell
aws s3 ls s3://<bucketname> --recursive  | grep -v -E "(Bucket: |Prefix: |LastWriteTime|^$|--)" | awk 'BEGIN {total=0}{total+=$3}END{print total/1024/1024" MB"}'
```


