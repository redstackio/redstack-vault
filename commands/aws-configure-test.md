---
id: new-uuid-1
type: command
executor: bash
data: aws sts get-caller-identity
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - aws
  - iam
  - verification
verified: true
validated: true
---

# aws-configure-test

## Command

```bash
aws sts get-caller-identity
```

## Description

This command tests AWS CLI configuration by retrieving the identity of the caller (account, user, and ARN). Use it to verify credentials and permissions before running IAM enumeration commands.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; uses default AWS profile | No |

## Examples

### Basic Usage

```bash
aws sts get-caller-identity
```

### With Specific Profile

```bash
aws sts get-caller-identity --profile myprofile
```

## Expected Output

```
{
    "UserId": "AIDAXYZ...",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/testuser"
}
```

A successful response confirms valid credentials. Errors like "AccessDenied" indicate permission issues.

## Related

- [[procedures/AWS-IAM-Group-Inline-Policies-Enumeration]]
- [[commands/aws-iam-list-group-policies]]
