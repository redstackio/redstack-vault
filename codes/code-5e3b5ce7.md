---
id: 5e3b5ce7-fc3f-4bc3-a34d-5b55ad7b7276
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:12.006026+00:00'
updated_at: '2023-04-10T20:19:59.615210+00:00'
---

# Code Snippet 5e3b5ce7

**Language**: Python

```python
import boto3
import json

def handler(event,context):
    iam = boto3.client("iam")
    # Attach policy to role
    iam.attach_role_policy(
        RoleName="name",
        PolicyArn="arn",
    )
    # Attach policy to user
    iam.attach_user_policy(
        UserName="name",
        PolicyArn="arn",
    )
    return {
        'statusCode':200,
        'body':json.dumps("IAM Policy Attached Successfully")
    }
```


