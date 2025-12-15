---
data: export AWS_PROFILE=PROFILE_NAME
tags:
  - aws
  - configuration
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 28f89134-68fb-444d-8010-2cdd720fc03b
created_at: '2025-12-14T17:32:39.218Z'
updated_at: '2025-12-14T17:32:39.218Z'
verified: false
validated: true
submitted: true
---
# Export AWS Profile

## Command

```bash
export AWS_PROFILE=PROFILE_NAME
```

## Description

Sets the AWS CLI to use a specific credential profile from the AWS credentials file, allowing authentication with different permission levels (e.g., admin or noperm) for API calls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `AWS_PROFILE` | Name of the profile from ~/.aws/credentials (e.g., admin, noperm) | Yes |

## Examples

### Basic Usage

```bash
export AWS_PROFILE=admin
```

### For Limited Permissions

```bash
export AWS_PROFILE=noperm
```

## Expected Output

No output; environment variable is set successfully. Verify with `echo $AWS_PROFILE`.

## Related

- [[commands/aws-datazone-list-domains]]
- [[procedures/Test-Non-Production-Endpoint-with-Admin-Credentials]]
