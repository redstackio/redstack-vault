---
id: c82067bc-c33f-42e2-b52a-51c168b97b58
name: aws-iam-list-roles
type: command
executor: bash
data: aws iam list-roles
output: null
created_at: '2023-04-06T03:56:10.802929+00:00'
updated_at: '2023-04-10T20:19:56.886823+00:00'
platforms:
  - AWS
  - Cloud
tags:
  - discovery
  - iam
  - cloud
verified: true
validated: true
---

# aws-iam-list-roles

## Command

```bash
aws iam list-roles
```

## Description

This command queries the AWS IAM service to retrieve a paginated list of all IAM roles in the current account. It is used during reconnaissance to map out role-based access controls without requiring elevated permissions beyond `iam:ListRoles`.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--output` | Specify output format (json, text, table). Defaults to json. | No |
| `--no-paginate` | Disable automatic pagination if dealing with many roles. | No |
| `--region` | AWS region to query (defaults to configured region). | No |
| `--profile` | AWS profile name if multiple configurations exist. | No |

## Examples

### Basic Usage

```bash
aws iam list-roles
```

### Advanced Usage

```bash
aws iam list-roles --output table --region us-east-1
```

## Expected Output

Successful execution returns a JSON object with a 'Roles' array:

```json
{
    "Roles": [
        {
            "Path": "/",
            "RoleName": "example-role",
            "RoleId": "AROAEXAMPLE",
            "Arn": "arn:aws:iam::123456789012:role/example-role",
            "CreateDate": "2023-01-01T00:00:00+00:00",
            "AssumeRolePolicyDocument": "...",
            "Description": "Example role"
        }
    ],
    "IsTruncated": false,
    "Marker": null
}
```

The 'IsTruncated' field indicates if more results are available; use `--max-items` or pagination tokens for large lists. Errors like 'AccessDenied' suggest insufficient permissions.
