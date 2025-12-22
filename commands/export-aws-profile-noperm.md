---
data: export AWS_PROFILE=noperm
tags:
  - aws
  - profile
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 2c94afb1-a082-4d1e-bc81-1cc5deac7332
created_at: '2025-12-14T17:32:39.014Z'
updated_at: '2025-12-14T17:32:39.014Z'
verified: false
validated: true
submitted: true
---
# export-aws-profile-noperm

## Command

```bash
export AWS_PROFILE=noperm
```

## Description

Sets the AWS CLI to use a non-privileged IAM profile for testing denied permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| AWS_PROFILE | Profile name (e.g., noperm) | Yes |

## Examples

### Basic Usage

```bash
export AWS_PROFILE=noperm
```

### Verify

```bash
echo $AWS_PROFILE
```

## Expected Output

Environment variable set; echo shows 'noperm'. Commands will reflect limited access.

## Related

- [[commands/export-aws-profile-admin]]
- [[procedures/Enumerate-IAM-Permissions-with-Profiles]]
