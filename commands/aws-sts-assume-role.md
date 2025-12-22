---
data: >-
  aws sts assume-role --role-arn
  arn:aws:iam::TARGET-ACCOUNT:role/TargetAdminRole --role-session-name
  exploit-session
tags:
  - sts
  - escalation
type: command
output: null
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.655Z'
id: 6c69f728-a8ca-4a9e-97a2-1f3984f66c24
verified: false
validated: true
submitted: true
---
# aws-sts-assume-role

## Command

```bash
aws sts assume-role --role-arn arn:aws:iam::TARGET-ACCOUNT:role/TargetAdminRole --role-session-name exploit-session
```

## Description

Assumes a role and returns temporary security credentials for that role.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--role-arn` | ARN of the role to assume | Yes |
| `--role-session-name` | Identifier for the session | Yes |

## Examples

### Basic Usage

```bash
aws sts assume-role --role-arn arn:... --role-session-name session1
```

## Expected Output

JSON with Credentials: {AccessKeyId, SecretAccessKey, SessionToken, Expiration}.

## Related

- [[commands/aws-s3-ls-with-creds]]
