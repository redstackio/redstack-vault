---
id: b2bcf595-ea2d-4c2c-b713-4649a1eebd9e
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:08.938062+00:00'
updated_at: '2023-04-10T20:20:58.743576+00:00'
---

# Code Snippet b2bcf595

**Language**: Python

```python
import boto3

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id='AKIAJQDP3RKREDACTED', aws_secret_access_key='igH8yFmmpMbnkcUaCqXJIRIozKVaREDACTED', region_name='us-west-1')

try:
    # List all S3 buckets
    result = s3.list_buckets()
    print(result)
except Exception as e:
    print(e)
```


