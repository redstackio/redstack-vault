---
data: 'curl http://169.254.169.254/latest/meta-data/iam/security-credentials/'
tags:
  - discovery
  - aws
type: command
executor: bash
platforms:
  - AWS
id: d531ab3b-e89a-4287-bc1e-27e853c77192
created_at: '2025-12-11T06:10:31.696Z'
updated_at: '2025-12-11T06:10:31.696Z'
verified: false
validated: true
submitted: true
---
# curl-aws-metadata-role

## Command

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

## Description

Retrieves the AWS IAM security credentials role name from instance metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

## Expected Output

Role name like ██████████

## Related

- [[commands/curl-aws-credentials]]
- [[procedures/Receive-and-Explore-Reverse-Shell]]
