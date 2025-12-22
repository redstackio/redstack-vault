---
id: 5a036d3b-135f-4ddc-95e9-66dc840334c1
name: aws-iam-list-access-keys
type: command
executor: bash
data: aws iam list-access-keys --user-name $_USERNAME
output: null
created_at: '2023-04-06T03:56:09.952153+00:00'
updated_at: '2023-04-10T20:20:23.589352+00:00'
platforms:
  - AWS
tags:
  - cloud-aws
  - iam-enumeration
verified: true
validated: true
---

# aws-iam-list-access-keys

## Command

```bash
aws iam list-access-keys --user-name $_USERNAME
```

## Description

This command lists all access keys for a specified IAM user in AWS. It retrieves metadata about the keys without exposing secret values, useful for auditing or identifying credentials during security assessments. Run it after authenticating via AWS CLI to target a specific user or the current one (omit --user-name).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--user-name` | The name of the IAM user (e.g., 'admin-user'). If omitted, lists keys for the authenticated user. | No |
| `--output` | Output format (json/text/table). Defaults to json. | No |
| `--query` | JMESPath query to filter output (e.g., 'AccessKeyMetadata[].AccessKeyId'). | No |
| `--no-paginate` | Disable automatic pagination for large results. | No |

## Examples

### Basic Usage

List keys for the current user:
```bash
aws iam list-access-keys
```

### Advanced Usage

List and filter for active keys only:
```bash
aws iam list-access-keys --user-name my-iam-user --query 'AccessKeyMetadata[?Status==`Active`].AccessKeyId' --output text
```

## Expected Output

Successful execution returns a JSON object like:
```json
{
    "AccessKeyMetadata": [
        {
            "UserName": "my-iam-user",
            "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "Status": "Active",
            "CreateDate": "2015-03-09T18:39:23.411Z"
        }
    ]
}
```
An empty array indicates no keys. Errors (e.g., AccessDenied) appear if permissions are insufficient.

## Related

- [[procedures/AWS-IAM-Access-Key-Enumeration]]
