---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: aws iam get-role --role-name rLambdaFunctionRole
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
updated_at: '2025-12-14T17:30:27.400Z'
verified: false
validated: true
submitted: true
---
# aws-iam-get-role

## Command

```bash
aws iam get-role --role-name rLambdaFunctionRole
```

## Description

Retrieves details of an IAM role, including ARN and assume role policy, to inspect permissions in AWS security assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--role-name` | Name of the IAM role | Yes |

## Examples

### Basic Usage

```bash
aws iam get-role --role-name rLambdaFunctionRole
```

### Advanced Usage

```bash
aws iam get-role --role-name rLambdaFunctionRole --output json
```

## Expected Output

JSON with role details: {"Role": {"Arn": "arn:aws:iam::123:role/rLambdaFunctionRole", ...}}

## Related

- [[Related Procedure]]
