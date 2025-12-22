---
id: new-uuid-1
name: aws-iam-create-role
type: command
executor: bash
data: >-
  aws iam create-role --role-name lambda-escalation-role
  --assume-role-policy-document
  '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}]
  }'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - iam
  - role-creation
verified: true
validated: true
---

# aws-iam-create-role

## Command

```bash
aws iam create-role --role-name $_ROLE_NAME --assume-role-policy-document '$_POLICY_DOCUMENT'
```

## Description

Creates a new IAM role that can be assumed by AWS services like Lambda. Used to set up a role for privilege escalation by attaching elevated policies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --role-name $_ROLE_NAME | Name of the role to create (e.g., lambda-escalation-role) | Yes |
| --assume-role-policy-document $_POLICY_DOCUMENT | JSON policy allowing assumption by a service (e.g., lambda.amazonaws.com) | Yes |

## Examples

### Basic Usage

```bash
aws iam create-role --role-name test-role --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}] }'
```

### Advanced Usage

Attach policy after creation:
```bash
aws iam attach-role-policy --role-name test-role --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
```

## Expected Output

```json
{
  "Role": {
    "Path": "/",
    "RoleName": "lambda-escalation-role",
    "RoleId": "AROAXXXXXXXXXXXX",
    "Arn": "arn:aws:iam::123456789012:role/lambda-escalation-role",
    "CreateDate": "2023-10-01T00:00:00Z",
    "AssumeRolePolicyDocument": { ... }
  }
}
```

## Related

- [[commands/aws-lambda-create-function]]
- [[procedures/aws-lambda-role-privilege-escalation]]
