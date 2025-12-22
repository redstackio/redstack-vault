---
id: 5db98607-2a48-48ee-a9d8-0ed13b32a3ba
name: aws-iam-create-access-key-for-user
type: command
executor: bash
data: aws iam create-access-key --user-name example_username
output: null
created_at: '2023-04-06T03:56:10.616322+00:00'
updated_at: '2023-04-10T20:20:01.298643+00:00'
platforms:
  - AWS
tags:
  - aws
  - iam
  - persistence
verified: true
validated: true
---

# aws-iam-create-access-key-for-user

## Command

```bash
aws iam create-access-key --user-name $_USERNAME
```

## Description

This command creates a new AWS access key (Access Key ID and Secret Access Key) for the specified IAM user, enabling programmatic authentication to AWS services. Use it when you have compromised credentials with IAM creation permissions to establish persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--user-name $_USERNAME` | The name of the IAM user for whom to create the access key (e.g., example_username) | Yes |

## Examples

### Basic Usage

```bash
aws iam create-access-key --user-name example_username
```

### Advanced Usage

To output in a specific format for scripting:

```bash
aws iam create-access-key --user-name example_username --output json
```

## Expected Output

Successful execution returns a JSON object with the new access key details:

```json
{
    "AccessKey": {
        "UserName": "example_username",
        "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "Status": "Active",
        "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        "CreateDate": "2023-04-06T03:56:10+00:00"
    }
}
```

The SecretAccessKey is shown only once; capture it immediately. Errors include `AccessDenied` if permissions are insufficient or `NoSuchEntity` if the user does not exist.

## Related

- [[commands/aws-iam-list-users]]
- [[commands/aws-iam-create-access-key-for-user]]
