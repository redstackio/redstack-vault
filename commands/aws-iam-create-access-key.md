---
id: 5db98607-2a48-48ee-a9d8-0ed13b32a3ba
name: aws-iam-create-access-key
type: command
executor: bash
data: aws iam create-access-key --user-name $_USER_NAME
output: null
created_at: '2023-04-06T03:56:10.616322+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - iam
  - persistence
verified: true
validated: true
---

# aws-iam-create-access-key

## Command

```bash
aws iam create-access-key --user-name $_USER_NAME
```

## Description

Creates a new access key pair for an IAM user to enable long-term API access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --user-name $_USER_NAME | Target IAM user | Yes |

## Examples

### Basic Usage

```bash
aws iam create-access-key --user-name target_user
```

## Expected Output

{
    "AccessKey": {
        "AccessKeyId": "AKIA...",
        "SecretAccessKey": "...",
        "CreateDate": "..."
    }
}

## Related

- [[procedures/AWS-Shadow-Admin-Access]]
