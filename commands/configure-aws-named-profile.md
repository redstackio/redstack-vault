---
id: b38194a0-7702-481d-bfab-cc21af7994d1
name: configure-aws-named-profile
type: command
executor: bash
data: aws configure --profile $_PROFILE_NAME
output: null
created_at: '2023-04-06T03:56:09.911128+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - configuration
  - aws
  - profile
verified: true
validated: true
---

# configure-aws-named-profile

## Command

```bash
aws configure --profile $_PROFILE_NAME
```

## Description

This command sets up a named AWS profile for isolated credential management, prompting for keys and settings specific to that profile name.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--profile $_PROFILE_NAME` | Specifies the profile name (e.g., victim-prod) | Yes |
| Interactive prompts | Same as default: $_ACCESS_KEY_ID, etc. | Yes |

## Examples

### Basic Usage

```bash
aws configure --profile victim-prod
# Enter credentials when prompted
```

### Usage in Commands

```bash
aws s3 ls --profile victim-prod
```

## Expected Output

Interactive prompts; files updated in ~/.aws/. Verify with `aws sts get-caller-identity --profile $_PROFILE_NAME`.

## Related

- [[procedures/Configure-AWS-CLI-for-S3-Access]]
- [[commands/configure-aws-default-profile]]
