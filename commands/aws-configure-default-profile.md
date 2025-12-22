---
id: 2ba5a6c8-ec11-4238-8166-e6a3d6dc741c
name: aws-configure-default-profile
type: command
executor: bash
data: aws configure
output: null
created_at: '2023-04-06T03:56:09.911058+00:00'
updated_at: '2023-04-10T20:19:56.523437+00:00'
platforms:
  - Linux
  - macOS
tags:
  - aws-cli
  - configuration
verified: true
validated: true
---

# aws-configure-default-profile

## Command

```bash
aws configure
```

## Description

This command interactively configures the default AWS CLI profile by prompting for AWS Access Key ID, Secret Access Key, default region name, and default output format. It is used to set up initial authentication for AWS services from the command line.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| AWS Access Key ID | Your 20-character access key (prompted) | Yes |
| AWS Secret Access Key | Your 40-character secret key (prompted) | Yes |
| Default region name | AWS region like us-east-1 (prompted) | Yes |
| Default output format | Format like json, text, or table (prompted) | Yes |

## Examples

### Basic Usage

```bash
aws configure
```

Enter values when prompted.

### Advanced Usage

For scripting, pre-populate via environment variables or files, but this command is interactive by default.

## Expected Output

No direct output; configuration is written to ~/.aws/config and ~/.aws/credentials. Success is confirmed by running `aws sts get-caller-identity` afterward, which returns account details without errors.

## Related

- [[procedures/AWS-CLI-Configuration]]
- [[commands/aws-configure-named-profile]]
