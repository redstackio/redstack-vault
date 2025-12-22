---
id: 3bc9dfeb-c503-463b-b513-4c548d244589
name: aws-iam-list-all-access-keys
type: command
executor: bash
data: |
  aws iam list-access-keys
output: null
created_at: '2020-07-31T04:25:28.972994+00:00'
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

# aws-iam-list-all-access-keys

## Command

```bash
aws iam list-access-keys
```

## Description

This command lists all IAM access keys in the AWS account, returning metadata such as user names, key IDs, creation dates, and status (Active or Inactive). Use it for initial reconnaissance to identify exposed credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; lists all keys account-wide | No |

## Examples

### Basic Usage

```bash
aws iam list-access-keys
```

### With Output Formatting (JSON Pretty-Print)

```bash
aws iam list-access-keys --output table
```

## Expected Output

```
{
    "AccessKeyMetadata": [
        {
            "UserName": "example-user",
            "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "Status": "Active",
            "CreateDate": "2015-03-09T18:39:23.411Z"
        }
    ]
}
```

A successful run returns a JSON object with an array of access key details. Empty array if no keys exist.

## Related

- [[procedures/List-AWS-IAM-Access-Keys]]
- [[commands/aws-iam-list-access-keys-for-user]]
