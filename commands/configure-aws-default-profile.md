---
id: ec645fc1-ae70-4679-a0af-bc12b9ac72cc
name: configure-aws-default-profile
type: command
executor: bash
data: aws configure
output: null
created_at: '2023-04-06T03:55:53.510841+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - configuration
  - aws
  - credentials
verified: true
validated: true
---

# configure-aws-default-profile

## Command

```bash
aws configure
```

## Description

This interactive command configures the default AWS profile by prompting for Access Key ID, Secret Access Key, region, and output format, storing them in ~/.aws/ files for authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Interactive prompts | Enter $_ACCESS_KEY_ID, $_SECRET_ACCESS_KEY, $_DEFAULT_REGION (e.g., us-east-1), $_OUTPUT_FORMAT (e.g., json) | Yes |

## Examples

### Basic Usage

```bash
aws configure
# Follow prompts:
AWS Access Key ID [None]: $_ACCESS_KEY_ID
AWS Secret Access Key [None]: $_SECRET_ACCESS_KEY
Default region name [None]: $_DEFAULT_REGION
Default output format [None]: $_OUTPUT_FORMAT
```

### Non-Interactive (via file)

Create ~/.aws/credentials manually with [default] section.

## Expected Output

No direct output; configuration files are updated. Verify with `aws sts get-caller-identity` returning account JSON.

## Related

- [[procedures/Configure-AWS-CLI-for-S3-Access]]
- [[commands/configure-aws-named-profile]]
