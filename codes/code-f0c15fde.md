---
id: f0c15fde-fb2f-4190-abc9-09608330b7f1
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:09.319291+00:00'
updated_at: '2023-04-10T20:19:54.707071+00:00'
---

# Code Snippet f0c15fde

**Language**: Python

```python
import boto3
def lambda_handler(event, context):
    client = boto3.client('iam')
    response = client.attach_user_policy(
    UserName='my_username',
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    )
    return response
```


