---
id: c4f8a67d-728c-487a-9667-1026e4f91a23
name: Configure-AWS-CLI-for-S3-Access
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:52.692671+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Application Access Token|T1527 - Application Access Token]]'
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/Amazon Bucket S3 AWS]]'
  - '[[tags/AWS Configuration]]'
  - cloud
  - credentials
commands:
  - '[[commands/install-aws-cli-on-ubuntu]]'
  - '[[commands/configure-aws-default-profile]]'
  - '[[commands/configure-aws-named-profile]]'
  - '[[commands/set-aws-environment-variables]]'
platforms:
  - Linux
  - IaaS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Configure-AWS-CLI-for-S3-Access

## Summary

This procedure outlines the steps to install and configure the AWS Command Line Interface (CLI) using compromised or provided AWS credentials, enabling interaction with S3 buckets for enumeration, data exfiltration, or misconfiguration testing in cloud environments. It covers installation on Debian-based systems, default profile setup, named profile creation, and environment variable configuration for temporary credentials.

## Description

In offensive security operations targeting AWS environments, attackers often obtain credentials through various means (e.g., phishing, misconfigurations). This procedure sets up the AWS CLI to authenticate and perform operations on S3 buckets, such as listing contents or downloading objects, while evading detection by using profiles or temporary tokens. It assumes access to a Linux attacker machine and valid AWS IAM credentials with S3 permissions. Proper configuration ensures seamless integration with tools like AWS CLI for lateral movement or data collection without relying on web consoles.

## Requirements

1. Valid AWS IAM credentials (Access Key ID, Secret Access Key, optional Session Token for temporary creds).
2. Debian-based Linux system (e.g., Ubuntu, Kali) with sudo access.
3. Internet connectivity for package installation and AWS API calls.
4. Basic knowledge of shell commands and AWS services.

## Defense

- Implement least-privilege IAM policies to limit S3 access for compromised credentials.
- Enable AWS CloudTrail logging for CLI API calls and monitor for unusual access patterns from external IPs.
- Use MFA and credential rotation; detect anomalous credential usage via AWS GuardDuty.
- Scan for exposed credentials in code repositories and enforce environment variable encryption.

## Objectives

1. Install AWS CLI to enable command-line interaction with AWS services.
2. Configure authentication for default and named profiles to support multiple credential sets.
3. Set up temporary credentials via environment variables for short-lived access tokens.
4. Verify setup by performing a basic S3 operation, ensuring secure access to target buckets.

## Instructions

### Step 1: Install AWS CLI on Ubuntu/Debian

**Context**: Install the AWS CLI package to provide the necessary tools for interacting with S3 and other AWS services from the command line. This step ensures the binary is available for subsequent configurations.

**Command** ([[commands/install-aws-cli-on-ubuntu]]):
```bash
sudo apt update && sudo apt install awscli -y
```

> This updates the package list and installs the AWS CLI. Run this as a privileged user. After installation, verify with `aws --version` to confirm the tool is ready (expected: version output like "aws-cli/2.x.x").

### Step 2: Configure Default AWS Profile

**Context**: Set up the default AWS profile with long-term credentials (Access Key ID and Secret Access Key) to authenticate API requests. This is the primary method for persistent access in testing scenarios.

**Command** ([[commands/configure-aws-default-profile]]):
```bash
aws configure
```

> When prompted interactively, enter the Access Key ID, Secret Access Key, default region (e.g., us-east-1), and output format (e.g., json). This creates ~/.aws/credentials and ~/.aws/config files. If credentials are invalid, subsequent commands will fail with authentication errors.

### Step 3: Configure Named AWS Profile

**Context**: Create a named profile for isolating different credential sets or environments, useful when testing multiple AWS accounts without overwriting the default configuration.

**Command** ([[commands/configure-aws-named-profile]]):
```bash
aws configure --profile $_PROFILE_NAME
```

> Replace $_PROFILE_NAME with a descriptive name (e.g., "victim-prod"). The interactive prompt will ask for credentials similar to the default profile. Use this profile in commands via `--profile $_PROFILE_NAME` to switch contexts. Verify by running `aws sts get-caller-identity --profile $_PROFILE_NAME` (expected: JSON with account details).

### Step 4: Set AWS Environment Variables for Temporary Credentials

**Context**: For temporary security tokens (e.g., from assumed roles), export credentials as environment variables. This overrides profile settings for session-based access, common in lateral movement after role assumption.

**Command** ([[commands/set-aws-environment-variables]]):
```bash
export AWS_ACCESS_KEY_ID="$_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="$_SECRET_ACCESS_KEY"
export AWS_SESSION_TOKEN="$_SESSION_TOKEN"
```

> Substitute the placeholders with actual values from the temporary credentials. These variables apply to the current shell session. Test with `aws s3 ls` (expected: list of accessible buckets if permissions allow). Note: Variables are lost on shell exit; re-export as needed.

### Step 5: Verify S3 Access

**Context**: Confirm the configuration by listing S3 buckets, ensuring credentials grant the necessary permissions for further operations like enumeration or exfiltration.

**Command** (using default profile):
```bash
aws s3 ls
```

> If using a named profile, add `--profile $_PROFILE_NAME`. Expected output: a list of bucket names if access is granted. Errors indicate permission issues or invalid credentials—troubleshoot by checking IAM policies.
