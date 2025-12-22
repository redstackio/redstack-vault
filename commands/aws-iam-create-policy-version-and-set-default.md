---
id: d2b911dd-951d-447b-b7e3-49b3faaf7b3f
name: aws-iam-create-policy-version-and-set-default
type: command
executor: bash
data: >-
  aws iam create-policy-version --policy-arn $_POLICY_ARN --policy-document
  file://$_POLICY_FILE --set-as-default; aws iam set-default-policy-version
  --policy-arn $_POLICY_ARN --version-id $_VERSION_ID
output: null
created_at: '2023-04-06T03:56:09.318776+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - iam
  - policy
verified: true
validated: true
---

# aws-iam-create-policy-version-and-set-default

## Command

```bash
aws iam create-policy-version --policy-arn $_POLICY_ARN --policy-document file://$_POLICY_FILE --set-as-default; aws iam set-default-policy-version --policy-arn $_POLICY_ARN --version-id $_VERSION_ID
```

## Description

Creates a new version of an IAM policy with escalated permissions and sets it as default.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --policy-arn $_POLICY_ARN | ARN of target policy | Yes |
| --policy-document file://$_POLICY_FILE | Path to new policy JSON | Yes |
| --version-id $_VERSION_ID | ID of version to set default | Yes (for second cmd) |

## Examples

### Basic Usage

```bash
aws iam create-policy-version --policy-arn arn:... --policy-document file://admin.json --set-as-default
```

## Expected Output

Version details; default set confirmation.

## Related

- [[procedures/AWS-Shadow-Admin-Access]]
