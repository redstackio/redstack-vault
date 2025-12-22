---
id: 06823711-ccdb-4a61-8dfd-6d8dee56336e
name: aws-iam-list-attached-role-policies
type: command
executor: bash
data: aws iam list-attached-role-policies --role-name $_ROLE_NAME
output: null
created_at: '2023-04-06T03:56:13.002565+00:00'
updated_at: '2023-04-10T20:19:59.274108+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - iam
  - discovery
verified: true
validated: true
---

# aws-iam-list-attached-role-policies

## Command

```bash
aws iam list-attached-role-policies --role-name $_ROLE_NAME
```

## Description

This command lists all managed policies attached to the specified IAM role in AWS. It is used during cloud discovery to enumerate permissions and identify potential escalation paths. Requires AWS CLI v2 and authenticated credentials with 'iam:ListAttachedRolePolicies' permission.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --role-name $_ROLE_NAME | The name of the IAM role to query (e.g., 'MyAppRole') | Yes |

## Examples

### Basic Usage

```bash
aws iam list-attached-role-policies --role-name MyEC2Role
```

### Advanced Usage

```bash
aws iam list-attached-role-policies --role-name MyEC2Role --output json | jq ".AttachedPolicies[] | select(.PolicyName == \"AdminPolicy\")"
```

## Expected Output

Successful execution returns a JSON object with an 'AttachedPolicies' array containing details for each policy:

```json
{
    "AttachedPolicies": [
        {
            "PolicyName": "AmazonS3ReadOnlyAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess",
            "AttachDate": "2023-01-15T12:00:00+00:00"
        }
    ]
}
```

If no policies are attached, the array is empty. Errors include 'AccessDenied' if permissions are insufficient.

## Related

- [[procedures/aws-iam-enumerate-attached-role-policies]]
- [[tools/aws-cli]]
