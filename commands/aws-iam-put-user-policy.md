---
id: de456e79-1bac-43e5-b912-abe1fcd13391
name: aws-iam-put-user-policy
type: command
executor: bash
data: >-
  aws iam put-user-policy --user-name $_USER_NAME --policy-name $_POLICY_NAME
  --policy-document file://$_POLICY_FILE
output: null
created_at: '2023-04-06T03:56:09.318405+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - iam
  - inline-policy
verified: true
validated: true
---

# aws-iam-put-user-policy

## Command

```bash
aws iam put-user-policy --user-name $_USER_NAME --policy-name $_POLICY_NAME --policy-document file://$_POLICY_FILE
```

## Description

Attaches an inline policy document to an IAM user for custom permission grants.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --user-name $_USER_NAME | Target user | Yes |
| --policy-name $_POLICY_NAME | Name for the inline policy | Yes |
| --policy-document file://$_POLICY_FILE | Path to JSON policy file | Yes |

## Examples

### Basic Usage

```bash
aws iam put-user-policy --user-name my_username --policy-name my_inline_policy --policy-document file://admin-policy.json
```

## Expected Output

No output on success.

## Related

- [[procedures/AWS-Shadow-Admin-Access]]
