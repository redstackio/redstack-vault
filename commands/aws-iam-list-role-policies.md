---
id: 5795b66c-bfaf-4e7d-abf8-1de384265c94
type: command
executor: bash
data: aws iam list-role-policies --role-name $_ROLE_NAME
output: null
created_at: '2023-04-06T03:56:10.239083+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - IAM
  - Discovery
  - Cloud
verified: true
validated: true
---

# aws-iam-list-role-policies

## Command

```bash
aws iam list-role-policies --role-name $_ROLE_NAME
```

## Description

This command lists the names of all inline policies embedded in the specified AWS IAM role. It is used during cloud discovery to identify permissions associated with the role, aiding in mapping access rights for potential exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --role-name $_ROLE_NAME | The name of the IAM role to query (e.g., 'MyAppRole') | Yes |

## Examples

### Basic Usage

```bash
aws iam list-role-policies --role-name MyEC2Role
```

### Advanced Usage

```bash
aws iam list-role-policies --role-name MyEC2Role --output table
```

## Expected Output

Successful execution returns a JSON object like:

```json
{
    "PolicyNames": [
        "InlinePolicy1",
        "S3AccessPolicy"
    ]
}
```

An empty 'PolicyNames' array indicates no inline policies. Errors appear as JSON with 'Error' key, such as {"__type":"AccessDeniedException"}.

## Related

- [[procedures/AWS-IAM-Role-Inline-Policy-Enumeration]]
- [[tools/AWS-CLI]]
