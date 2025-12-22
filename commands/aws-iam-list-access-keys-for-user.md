---
id: ec94634d-a132-4d4d-b0eb-36bf31dd1b89
name: aws-iam-list-access-keys-for-user
type: command
executor: bash
data: |
  aws iam list-access-keys --user-name $AWS_IAM_USER
output: null
created_at: '2020-07-31T04:25:28.973184+00:00'
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

# aws-iam-list-access-keys-for-user

## Command

```bash
aws iam list-access-keys --user-name $_AWS_IAM_USER
```

## Description

This command retrieves IAM access keys for a specific user, useful for targeted discovery of credentials tied to high-privilege accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --user-name $_AWS_IAM_USER | The IAM username (e.g., 'admin') | Yes |

## Examples

### Basic Usage

```bash
aws iam list-access-keys --user-name admin-user
```

### With JSON Output

```bash
aws iam list-access-keys --user-name admin-user --output json
```

## Expected Output

```
{
    "AccessKeyMetadata": [
        {
            "UserName": "admin-user",
            "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "Status": "Active",
            "CreateDate": "2015-03-09T18:39:23.411Z"
        }
    ]
}
```

Returns user-specific key metadata or an empty array if none exist.

## Related

- [[procedures/List-AWS-IAM-Access-Keys]]
- [[commands/aws-iam-list-all-access-keys]]
