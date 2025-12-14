---
data: export AWS_PROFILE=admin
tags:
  - aws
  - profile
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: f5e29e2d-aa07-4074-bdb3-346c15fab002
created_at: '2025-12-14T17:32:39.020Z'
updated_at: '2025-12-14T17:32:39.020Z'
verified: false
validated: true
submitted: true
---
# export-aws-profile-admin

## Command

```bash
export AWS_PROFILE=admin
```

## Description

Sets the AWS CLI to use an administrative IAM profile for subsequent commands, enabling privileged testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| AWS_PROFILE | Profile name (e.g., admin) | Yes |

## Examples

### Basic Usage

```bash
export AWS_PROFILE=admin
```

### Verify

```bash
echo $AWS_PROFILE
```

## Expected Output

Environment variable set; echo shows 'admin'. Subsequent AWS commands use this profile.

## Related

- [[commands/export-aws-profile-noperm]]
- [[procedures/Enumerate-IAM-Permissions-with-Profiles]]
