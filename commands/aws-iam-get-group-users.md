---
id: dc64ebf8-f654-4a72-bad5-5ccb58ba1a3a
name: aws-iam-get-group-users
type: command
executor: bash
data: |
  aws iam get-group --group-name $_AWS_IAM_GROUP
output: null
created_at: '2020-07-31T04:25:31.048450+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - aws
  - iam
  - discovery
verified: true
validated: true
---

# aws-iam-get-group-users

## Command

```bash
aws iam get-group --group-name $_AWS_IAM_GROUP
```

## Description

This command fetches details of a specific IAM group, including its member users. Use it to enumerate users in targeted groups like admin groups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--group-name $_AWS_IAM_GROUP` | The name of the IAM group to query (e.g., "Admins"). Set via environment variable or directly. | Yes |

## Examples

### Basic Usage

```bash
AWS_IAM_GROUP="Admins" && aws iam get-group --group-name $AWS_IAM_GROUP
```

### With JSON Path Query

```bash
aws iam get-group --group-name Admins | jq '.Users[].UserName'
```

## Expected Output

```
{
    "Group": {
        "GroupName": "Admins",
        "GroupId": "GIDAXYZ",
        "Arn": "arn:aws:iam::123456789012:group/Admins",
        "CreateDate": "2023-01-01T00:00:00Z"
    },
    "Users": [
        {
            "UserName": "admin-user",
            "Path": "/",
            "UserId": "AIDAXYZ",
            "Arn": "arn:aws:iam::123456789012:user/admin-user",
            "CreateDate": "2023-01-01T00:00:00Z"
        }
    ]
}
```
Includes group info and a `Users` array. Errors if group not found.

## Related

- [[procedures/Enumerate-AWS-IAM-Users-and-Groups]]
- [[commands/aws-iam-list-groups]]
