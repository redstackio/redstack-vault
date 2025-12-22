---
id: 8bf2a2d9-f06a-4b72-9674-072dcfb0a20f
name: AWS-CLI-Configuration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.917204+00:00'
updated_at: '2023-04-10T20:19:56.506917+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques:
  - '[[Credentials in Files]]'
  - '[[Credentials in Registry]]'
  - '[[Bash History]]'
  - '[[Private Keys]]'
tags:
  - cloud-aws
  - aws-cli-configuration
commands:
  - '[[commands/aws-configure-default-profile]]'
  - '[[commands/check-aws-credentials-file-existence]]'
  - '[[commands/aws-configure-named-profile]]'
platforms:
  - Linux
  - macOS
tools: []
validated: true
---

# AWS-CLI-Configuration

## Summary

This procedure outlines the steps to configure the AWS Command Line Interface (CLI) on a local machine using access keys and secret keys, enabling interaction with AWS services for management, automation, or security testing scenarios such as accessing resources with compromised credentials.

## Description

Configuring the AWS CLI involves setting up authentication credentials, default region, and output format to allow command-line access to AWS resources. In security contexts, this is often used after obtaining unsecured credentials (e.g., from files, history, or registry) to perform reconnaissance, data exfiltration, or privilege escalation in cloud environments. The process stores credentials in the ~/.aws/credentials file and configuration in ~/.aws/config, which can expose sensitive information if not secured properly. This procedure assumes the AWS CLI is already installed and focuses on credential setup for default or named profiles.

## Requirements

1. AWS account with IAM user permissions to generate access keys.
2. AWS CLI installed on the local machine (version 2 recommended).
3. Access Key ID and Secret Access Key obtained from AWS IAM console.
4. Local shell environment (Bash on Linux/macOS).

## Defense

- Enable MFA for all IAM users and rotate access keys regularly.
- Use IAM roles instead of long-term access keys where possible.
- Monitor AWS CloudTrail for unusual CLI access patterns and credential usage.
- Restrict credential storage to encrypted volumes and avoid committing ~/.aws/ to version control.

## Objectives

1. Set up AWS CLI with authentication credentials for secure resource access.
2. Create named profiles for managing multiple AWS accounts or environments.
3. Verify credential file existence and configuration integrity.
4. Enable automated or scripted interactions with AWS services.

## Instructions

### Step 1: Configure Default AWS Profile

**Context**: This step initializes the default AWS CLI profile by prompting for Access Key ID, Secret Access Key, default region (e.g., us-east-1), and output format (e.g., json). It creates or updates the ~/.aws/config and ~/.aws/credentials files, allowing immediate use of AWS commands without specifying a profile.

**Command** ([[commands/aws-configure-default-profile]]):
```bash
aws configure
```

> Run this command in your terminal. It will interactively prompt for the four values. Use 'json' for output format to enable easy parsing in scripts. Upon completion, credentials are stored securely in the home directory files.

### Step 2: Verify AWS Credentials File Existence

**Context**: After configuration, check if the credentials file has been created correctly. This step confirms the presence of ~/.aws/credentials, which contains the sensitive keys in INI format, helping to validate setup before proceeding to AWS operations.

**Command** ([[commands/check-aws-credentials-file-existence]]):
```bash
ls ~/.aws/credentials
```

> If the file exists, the command lists it without errors. If not, it indicates configuration failure (e.g., permission issues). Inspect the file contents manually if needed, but avoid logging or sharing it.

### Step 3: Configure Named AWS Profile

**Context**: For scenarios involving multiple AWS accounts (e.g., testing different environments), create a named profile like 'test' or 'prod'. This isolates credentials and allows switching via --profile flag, reducing risk of using wrong keys in security assessments.

**Command** ([[commands/aws-configure-named-profile]]):
```bash
aws configure --profile test-profile
```

> Replace 'test-profile' with your desired name. The prompts are the same as default configuration. Use this profile in commands like `aws s3 ls --profile test-profile` to target specific credentials.
