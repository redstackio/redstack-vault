---
id: f347b86f-f7fd-4695-a587-65ffdfeafbff
name: aws-iam-get-user-policy
type: command
executor: bash
data: aws iam get-user-policy --user-name $_USER_NAME --policy-name $_POLICY_NAME
output: null
created_at: '2023-04-06T03:56:10.365156+00:00'
updated_at: '2023-04-10T20:20:04.832422+00:00'
platforms:
  - AWS
tags:
  - iam
  - enumeration
verified: true
validated: true
---

# aws-iam-get-user-policy

## Command

```bash
aws iam get-user-policy --user-name $_USER_NAME --policy-name $_POLICY_NAME
```

## Description

Retrieves the specified inline policy document embedded in an IAM user. Use this during AWS reconnaissance to inspect user permissions for privilege escalation opportunities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --user-name $_USER_NAME | The name of the IAM user (e.g., "john.doe") | Yes |
| --policy-name $_POLICY_NAME | The name of the inline policy (e.g., "CustomPolicy") | Yes |

## Examples

### Basic Usage

```bash
aws iam get-user-policy --user-name john.doe --policy-name AdminAccess
```

### Advanced Usage

```bash
aws iam get-user-policy --user-name john.doe --policy-name S3ReadOnly --output json
```

## Expected Output

Successful execution returns JSON with the policy details:

```json
{
    "UserName": "john.doe",
    "PolicyName": "AdminAccess",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }
}
```

If the policy does not exist, it returns an error like "An error occurred (NoSuchEntity) when calling the GetUserPolicy operation".

## Related

- [[procedures/Enumerate-AWS-IAM-Inline-Policies]]
- [[commands/aws-iam-get-group-policy]]
