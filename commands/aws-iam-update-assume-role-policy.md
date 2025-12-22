---
id: 37322e9a-67a0-4989-a72b-116b6ad3baf2
name: aws-iam-update-assume-role-policy
type: command
executor: bash
data: >-
  aws iam update-assume-role-policy --role-name $_ROLE_NAME --policy-document
  file://$_POLICY_FILE
output: null
created_at: '2023-04-06T03:56:09.318650+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - iam
  - role
verified: true
validated: true
---

# aws-iam-update-assume-role-policy

## Command

```bash
aws iam update-assume-role-policy --role-name $_ROLE_NAME --policy-document file://$_POLICY_FILE
```

## Description

Updates the trust policy of an IAM role to allow assumption by unauthorized principals.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --role-name $_ROLE_NAME | Target role | Yes |
| --policy-document file://$_POLICY_FILE | Path to updated trust policy JSON | Yes |

## Examples

### Basic Usage

```bash
aws iam update-assume-role-policy --role-name role_i_can_assume --policy-document file://trust.json
```

## Expected Output

No output on success.

## Related

- [[procedures/AWS-Shadow-Admin-Access]]
