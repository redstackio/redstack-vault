---
data: 'curl http://169.254.169.254/latest/meta-data/iam/security-credentials/'
tags:
  - exfil
  - aws
type: command
output: '[redacted-role-name]'
executor: bash
platforms:
  - Linux
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.374Z'
id: 81299331-5547-44fb-bad2-f3d4fb4892bc
verified: false
validated: true
submitted: true
---
# curl-aws-iam-roles

## Command

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

## Description

Retrieves the list of IAM roles from AWS instance metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Metadata endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

## Expected Output

[redacted-role-name]

## Related

- [[commands/curl-aws-iam-credentials]]
