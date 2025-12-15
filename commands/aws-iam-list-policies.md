---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: aws iam list-attached-role-policies --role-name rLambdaFunctionRole
tags:
  - aws
  - iam
  - inspection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:27.395Z'
verified: false
validated: true
submitted: true
---
# aws-iam-list-policies

## Command

```bash
aws iam list-attached-role-policies --role-name rLambdaFunctionRole
```

## Description

Lists policies attached to an IAM role to identify overly permissive attachments like AdministratorAccess.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--role-name` | Name of the IAM role | Yes |

## Examples

### Basic Usage

```bash
aws iam list-attached-role-policies --role-name rLambdaFunctionRole
```

### Advanced Usage

```bash
aws iam list-attached-role-policies --role-name rLambdaFunctionRole --query 'AttachedPolicies[?PolicyName==`AdministratorAccess`]'
```

## Expected Output

JSON array of attached policies, including AdministratorAccess.

## Related

- [[Related Procedure]]
