---
id: 8e39f9b1-a146-4d0e-8bd9-30b71acf092d
name: aws-iam-list-groups
type: command
executor: bash
data: aws iam list-groups
output: null
created_at: '2023-04-06T03:56:10.111561+00:00'
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

# aws-iam-list-groups

## Command

```bash
aws iam list-groups
```

## Description

This command lists all IAM groups in the authenticated AWS account, returning details like group names, IDs, ARNs, and creation dates in JSON format. Use it during discovery to map permission structures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters required; uses default AWS CLI configuration for authentication and region. | No |

## Examples

### Basic Usage

```bash
aws iam list-groups
```

### With JSON Formatting (using jq)

```bash
aws iam list-groups | jq '.Groups[] | {GroupName, Arn}'
```

## Expected Output

Successful execution returns a JSON object with a "Groups" array:

```json
{
    "Groups": [
        {
            "Path": "/",
            "GroupName": "Developers",
            "GroupId": "AIDAITDJ3ZJQRJ4EXAMPLE",
            "Arn": "arn:aws:iam::123456789012:group/Developers",
            "CreateDate": "2015-03-09T18:39:32.090Z"
        }
    ],
    "IsTruncated": false
}
```

If no groups exist, "Groups" is an empty array. Errors like "AccessDenied" indicate insufficient permissions.

## Related

- [[procedures/AWS-IAM-Group-Enumeration]]
- [[tools/aws-cli]]
