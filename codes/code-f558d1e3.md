---
id: f558d1e3-7cf2-40e4-8d98-46beaa085f27
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:53.656091+00:00'
updated_at: '2023-04-06T03:55:53.663227+00:00'
---

# Code Snippet f558d1e3

**Language**: Powershell

```powershell
aws s3 ls s3://<bucketname> --recursive  | grep -v -E "(Bucket: |Prefix: |LastWriteTime|^$|--)" | awk 'BEGIN {total=0}{total+=$3}END{print total/1024/1024" MB"}'
```


