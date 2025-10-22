---
id: 384a0162-2cba-4dfc-accd-48a8cd8a226d
name: Attach IAM policy to user
type: command
executor: bash
data: "import boto3\ndef lambda_handler(event, context):\n    client = boto3.client('iam')\n\
  \    response = client.attach_user_policy(\n    UserName='my_username',\n    PolicyArn=\"\
  arn:aws:iam::aws:policy/AdministratorAccess\"\n    )\n    return response"
output: null
created_at: '2023-04-06T03:56:09.319394+00:00'
updated_at: '2023-04-10T20:19:54.703524+00:00'
---

# Attach IAM policy to user

```bash
import boto3
def lambda_handler(event, context):
    client = boto3.client('iam')
    response = client.attach_user_policy(
    UserName='my_username',
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    )
    return response
```
