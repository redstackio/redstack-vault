---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: aws-iam-create-user
type: command
executor: bash
data: aws iam create-user --user-name $_USER_NAME
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - iam
  - persistence
verified: true
validated: true
---

# AWS IAM Create User

## Command

```bash
aws iam create-user --user-name $_USER_NAME
```

## Description

This command creates a new IAM user in the AWS account, which can be used as a backdoor for persistence. It requires IAM permissions to create users and is typically run after initial compromise to establish long-term access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --user-name $_USER_NAME | The name of the IAM user to create (e.g., backdoor-user) | Yes |
| -h, --help | Show help for the command | No |

## Examples

### Basic Usage

```bash
aws iam create-user --user-name backdoor-user
```

### With Output to File

```bash
aws iam create-user --user-name backdoor-user --output text > user_arn.txt
```

## Expected Output

Successful execution returns a JSON object describing the new user:

```json
{
  "User": {
    "Path": "/",
    "UserName": "backdoor-user",
    "UserId": "AIDAXYZ1234567890",
    "Arn": "arn:aws:iam::123456789012:user/backdoor-user",
    "CreateDate": "2023-10-01T12:00:00Z"
  }
}
```

Error example (insufficient permissions):

```json
{
  "Error": {
    "Code": "AccessDenied",
    "Message": "User is not authorized..."
  }
}
```

## Related

- [[procedures/configure-aws-cli-profile-for-persistence]]
- [[tools/aws-cli]]
