---
id: 5ab2b8f0-70f2-456b-9703-c3a42bc8661d
name: aws-iam-attach-admin-policy-to-user
type: command
executor: bash
data: >-
  aws iam attach-user-policy --user-name $_USER_NAME --policy-arn
  arn:aws:iam::aws:policy/AdministratorAccess
output: null
created_at: '2023-04-06T03:56:09.318220+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - iam
  - privilege-escalation
verified: true
validated: true
---

# aws-iam-attach-admin-policy-to-user

## Command

```bash
aws iam attach-user-policy --user-name $_USER_NAME --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

## Description

Attaches the AWS AdministratorAccess policy to an IAM user for immediate admin access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --user-name $_USER_NAME | Name of the target user | Yes |
| --policy-arn | ARN of AdministratorAccess | Yes |

## Examples

### Basic Usage

```bash
aws iam attach-user-policy --user-name my_username --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

## Expected Output

Success with no output; verify via list-attached-user-policies.

## Related

- [[procedures/AWS-Shadow-Admin-Access]]
