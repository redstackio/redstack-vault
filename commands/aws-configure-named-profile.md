---
id: f5f306be-e181-4c99-9fe8-335db5a492d4
name: aws-configure-named-profile
type: command
executor: bash
data: aws configure --profile $_PROFILE_NAME
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - configuration
  - persistence
verified: true
validated: true
---

# AWS Configure Named Profile

## Command

```bash
aws configure --profile $_PROFILE_NAME
```

## Description

This interactive command sets up a named profile in AWS CLI configuration files, storing access keys, region, and output format for specific AWS accounts or users. It's used in persistence scenarios to create isolated credential stores for backdoor access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --profile $_PROFILE_NAME | The name of the profile to create/update (e.g., backdoor-profile) | Yes |
| -h, --help | Show help for the command | No |

## Examples

### Basic Usage

```bash
aws configure --profile backdoor-profile
```

(Interactive: Enter Access Key ID, Secret Access Key, region, output format.)

### Non-Interactive (Advanced)

```bash
aws configure set aws_access_key_id $_ACCESS_KEY --profile $_PROFILE_NAME
aws configure set aws_secret_access_key $_SECRET_KEY --profile $_PROFILE_NAME
aws configure set region us-east-1 --profile $_PROFILE_NAME
```

## Expected Output

No direct output; runs interactively with prompts:

AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI...
Default region name [None]: us-east-1
Default output format [None]: json

Post-execution, verify with: cat ~/.aws/credentials (shows [backdoor-profile] section).

## Related

- [[procedures/configure-aws-cli-profile-for-persistence]]
- [[tools/aws-cli]]
