---
id: 5ffae73d-632a-4302-827c-387e642f2cd9
name: aws-iam-list-attached-group-policies
type: command
executor: bash
data: aws iam list-attached-group-policies --group-name $_GROUP_NAME
output: null
created_at: '2023-04-06T03:56:10.135305+00:00'
updated_at: '2023-04-10T20:19:46.679347+00:00'
platforms:
  - AWS
tags:
  - cloud
  - iam
  - enumeration
verified: true
validated: true
---

# aws-iam-list-attached-group-policies

## Command

```bash
aws iam list-attached-group-policies --group-name $_GROUP_NAME
```

## Description

This command queries the AWS IAM service to list all managed policies attached to a specified IAM group. It is used during cloud reconnaissance to discover permissions granted to group members, aiding in identifying escalation or lateral movement opportunities. Run this in a terminal with AWS CLI configured.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--group-name $_GROUP_NAME` | The name of the IAM group to query (e.g., "Developers" or "Admins") | Yes |

## Examples

### Basic Usage

```bash
aws iam list-attached-group-policies --group-name Admins
```

### Advanced Usage with Output Parsing

```bash
aws iam list-attached-group-policies --group-name Admins --output json | jq '.AttachedPolicies[] | .PolicyName'
```

## Expected Output

Successful execution returns a JSON object like:

```json
{
    "AttachedPolicies": [
        {
            "PolicyName": "AdministratorAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess"
        }
    ],
    "IsTruncated": false
}
```

If no policies are attached, "AttachedPolicies" is an empty array. Errors occur if credentials lack permissions (e.g., AccessDenied).

## Related

- [[procedures/AWS-IAM-Group-Managed-Policies-Enumeration]]
