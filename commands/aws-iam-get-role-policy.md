---
id: 58e52b13-23dd-42d9-baef-859d46add3c8
name: aws-iam-get-role-policy
type: command
executor: bash
data: aws iam get-role-policy --role-name $_ROLE_NAME --policy-name $_POLICY_NAME
output: null
created_at: '2023-04-06T03:56:10.365290+00:00'
updated_at: '2023-04-10T20:20:04.832422+00:00'
platforms:
  - AWS
tags:
  - iam
  - enumeration
verified: true
validated: true
---

# aws-iam-get-role-policy

## Command

```bash
aws iam get-role-policy --role-name $_ROLE_NAME --policy-name $_POLICY_NAME
```

## Description

Retrieves the specified inline policy document embedded in an IAM role. Useful for discovering assumable roles and their permissions during privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --role-name $_ROLE_NAME | The name of the IAM role (e.g., "EC2AdminRole") | Yes |
| --policy-name $_POLICY_NAME | The name of the inline policy (e.g., "RolePolicy") | Yes |

## Examples

### Basic Usage

```bash
aws iam get-role-policy --role-name EC2AdminRole --policy-name FullAccess
```

### Advanced Usage

```bash
aws iam get-role-policy --role-name EC2AdminRole --policy-name FullAccess --query 'PolicyDocument'
```

## Expected Output

Successful execution returns JSON with the policy details:

```json
{
    "RoleName": "EC2AdminRole",
    "PolicyName": "FullAccess",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "ec2:*",
                "Resource": "*"
            }
        ]
    }
}
```

Error if not found: "NoSuchEntity" for the role or policy.

## Related

- [[procedures/Enumerate-AWS-IAM-Inline-Policies]]
- [[commands/aws-iam-get-group-policy]]
