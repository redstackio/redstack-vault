---
id: 82001a88-de85-4053-b67f-4701db131de7
name: aws-iam-list-user-policies
type: command
executor: bash
data: aws iam list-user-policies --user-name example_user
output: null
created_at: '2023-04-06T03:56:10.564853+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - aws
  - iam
  - discovery
verified: true
validated: true
---

# aws-iam-list-user-policies

## Command

```bash
aws iam list-user-policies --user-name $_USER_NAME
```

## Description

This command lists all inline policies attached to the specified IAM user, returning their names for further analysis of permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --user-name $_USER_NAME | The name of the IAM user (e.g., example_user) | Yes |

## Examples

### Basic Usage

```bash
aws iam list-user-policies --user-name example_user
```

### With JSON Output Specified

```bash
aws iam list-user-policies --user-name example_user --output json
```

## Expected Output

```json
{
    "PolicyNames": [
        "InlinePolicy1",
        "CustomAdminPolicy"
    ]
}
```

Success returns a JSON object with a `PolicyNames` array listing inline policy names. An empty array indicates no inline policies.

## Related

- [[procedures/AWS-IAM-Inline-Policy-Enumeration]]
- [[commands/aws-sts-get-caller-identity]]
