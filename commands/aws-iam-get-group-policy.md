---
id: be25065a-93ab-44a6-adf1-6eae26072a88
name: aws-iam-get-group-policy
type: command
executor: bash
data: aws iam get-group-policy --group-name $_GROUP_NAME --policy-name $_POLICY_NAME
output: null
created_at: '2023-04-06T03:56:10.365225+00:00'
updated_at: '2023-04-10T20:20:04.832422+00:00'
platforms:
  - AWS
tags:
  - iam
  - enumeration
verified: true
validated: true
---

# aws-iam-get-group-policy

## Command

```bash
aws iam get-group-policy --group-name $_GROUP_NAME --policy-name $_POLICY_NAME
```

## Description

Retrieves the specified inline policy document embedded in an IAM group. This helps enumerate shared permissions across group members for lateral movement assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --group-name $_GROUP_NAME | The name of the IAM group (e.g., "Admins") | Yes |
| --policy-name $_POLICY_NAME | The name of the inline policy (e.g., "GroupPolicy") | Yes |

## Examples

### Basic Usage

```bash
aws iam get-group-policy --group-name Admins --policy-name ReadOnlyAccess
```

### Advanced Usage

```bash
aws iam get-group-policy --group-name Admins --policy-name ReadOnlyAccess --output table
```

## Expected Output

Successful execution returns JSON with the policy details:

```json
{
    "GroupName": "Admins",
    "PolicyName": "ReadOnlyAccess",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:GetObject",
                "Resource": "*"
            }
        ]
    }
}
```

Error if policy not found: "NoSuchEntity" exception.

## Related

- [[procedures/Enumerate-AWS-IAM-Inline-Policies]]
- [[commands/aws-iam-get-user-policy]]
